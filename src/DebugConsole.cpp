#include "DebugConsole.hpp"

#ifdef DEBUG_CONSOLE

#include <SDL2/SDL.h>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include "AnmManager.hpp"
#include "AsciiManager.hpp"
#include "BombData.hpp"
#include "BulletManager.hpp"
#include "Chain.hpp"
#include "ChainPriorities.hpp"
#include "EclManager.hpp"
#include "EnemyManager.hpp"
#include "GameManager.hpp"
#include "GameWindow.hpp"
#include "Gui.hpp"
#include "MainMenu.hpp"
#include "Player.hpp"
#include "ReplayManager.hpp"
#include "ScreenEffect.hpp"
#include "Stage.hpp"
#include "Supervisor.hpp"
#include "utils.hpp"

// Layout. AsciiManager strings hold 63 characters at most, so CONSOLE_COLUMNS can't go past that.
#define CONSOLE_COLUMNS 60
#define CONSOLE_LOG_LINES 16
#define CONSOLE_TEXT_SCALE 0.75f
#define CONSOLE_LINE_HEIGHT 12.0f
#define CONSOLE_PADDING 4.0f
#define CONSOLE_HEIGHT (CONSOLE_LINE_HEIGHT * (CONSOLE_LOG_LINES + 1) + CONSOLE_PADDING * 2)
#define CONSOLE_SLIDE_MS 500.0f

#define CONSOLE_PROMPT "> "
// Leaves room for the prompt and the cursor.
#define CONSOLE_INPUT_MAX (CONSOLE_COLUMNS - 3)
#define CONSOLE_HISTORY_LINES 16
#define CONSOLE_MAX_ARGS 16

#define CONSOLE_COLOR_BACKGROUND 0xb0003000
#define CONSOLE_COLOR_BORDER 0xff00c000
#define CONSOLE_COLOR_TEXT 0xff40ff40
#define CONSOLE_COLOR_ECHO 0xffc0ffc0
#define CONSOLE_COLOR_ERROR 0xffff6060
#define CONSOLE_COLOR_BAT_HITBOX 0x80ff2020

// Stage timeline opcodes, see EnemyManager::RunEclTimeline.
#define TIMELINE_OPCODE_LAST_SPAWN 7
#define TIMELINE_OPCODE_DIALOGUE 8
// A boss that flies in right before its dialogue has to be kept when skipping to that dialogue.
#define SKIP_LEAD_IN_FRAMES 120

#define MAX_LIVES 8
#define MAX_BOMBS 8
#define MAX_POWER 128

struct ConsoleLine
{
    char text[CONSOLE_COLUMNS + 1];
    ZunColor color;
};

struct ConsoleCommand
{
    const char *name;
    const char *usage;
    void (*run)(i32 argc, char **argv);
};

struct ConsoleName
{
    const char *name;
    i32 value;
};

static ChainElem g_DebugConsoleCalcChain;
static ChainElem g_DebugConsoleDrawChain;

static bool g_IsOpen;
static bool g_GodMode;
static bool g_ShowBatHitbox;
// 0 when fully hidden, 1 when fully dropped down.
static f32 g_SlideProgress;
static u32 g_LastDrawTime;

static ConsoleLine g_Log[CONSOLE_LOG_LINES];
static char g_Input[CONSOLE_INPUT_MAX + 1];
static i32 g_InputLength;
static char g_History[CONSOLE_HISTORY_LINES][CONSOLE_INPUT_MAX + 1];
static i32 g_HistoryCount;
// Index into g_History while browsing with up/down, g_HistoryCount when editing a fresh line.
static i32 g_HistoryCursor;

static const ConsoleName g_CharacterNames[] = {
    {"reimu", CHARA_REIMU},
    {"marisa", CHARA_MARISA},
    {"poyo", CHARA_POYO},
};

static const ConsoleName g_ShotTypeNames[] = {
    {"a", SHOT_TYPE_A},
    {"b", SHOT_TYPE_B},
};

static const ConsoleName g_DifficultyNames[] = {
    {"easy", EASY}, {"normal", NORMAL}, {"hard", HARD}, {"lunatic", LUNATIC}, {"extra", EXTRA},
};

static void AddLogLine(const char *text, i32 length, ZunColor color)
{
    std::memmove(&g_Log[0], &g_Log[1], sizeof(g_Log) - sizeof(g_Log[0]));

    ConsoleLine *line = &g_Log[CONSOLE_LOG_LINES - 1];
    std::memcpy(line->text, text, length);
    line->text[length] = '\0';
    line->color = color;
}

static void PrintColored(ZunColor color, const char *fmt, std::va_list args)
{
    char buffer[512];
    const char *lineStart;
    const char *cursor;

    std::vsnprintf(buffer, sizeof(buffer), fmt, args);
    utils::DebugPrint2("[console] %s\n", buffer);

    // Split on newlines, and wrap whatever doesn't fit on one line.
    lineStart = buffer;
    for (cursor = buffer;; cursor++)
    {
        if (*cursor == '\n' || *cursor == '\0' || cursor - lineStart == CONSOLE_COLUMNS)
        {
            AddLogLine(lineStart, cursor - lineStart, color);
            if (*cursor == '\0')
            {
                break;
            }
            lineStart = *cursor == '\n' ? cursor + 1 : cursor;
        }
    }
}

static void Print(const char *fmt, ...)
{
    std::va_list args;

    va_start(args, fmt);
    PrintColored(CONSOLE_COLOR_TEXT, fmt, args);
    va_end(args);
}

static void PrintError(const char *fmt, ...)
{
    std::va_list args;

    va_start(args, fmt);
    PrintColored(CONSOLE_COLOR_ERROR, fmt, args);
    va_end(args);
}

static void SetOpen(bool isOpen)
{
    g_IsOpen = isOpen;
    g_HistoryCursor = g_HistoryCount;

    // Text input is normally kept off so IMEs don't get in the way of the game (see Controller::ResetKeyboard).
    if (isOpen)
    {
        SDL_StartTextInput();
    }
    else
    {
        SDL_StopTextInput();
    }
}

static bool ParseInt(const char *text, i32 *out)
{
    char *end;
    long value;

    value = std::strtol(text, &end, 10);
    if (end == text || *end != '\0')
    {
        return false;
    }

    *out = (i32)value;
    return true;
}

// Accepts either one of the names, or the number it stands for.
static bool ParseName(const char *text, const ConsoleName *names, i32 numNames, i32 *out)
{
    i32 idx;
    i32 value;

    for (idx = 0; idx < numNames; idx++)
    {
        if (std::strcmp(text, names[idx].name) == 0)
        {
            *out = names[idx].value;
            return true;
        }
    }

    if (ParseInt(text, &value))
    {
        for (idx = 0; idx < numNames; idx++)
        {
            if (names[idx].value == value)
            {
                *out = value;
                return true;
            }
        }
    }

    return false;
}

static const char *NameOf(const ConsoleName *names, i32 numNames, i32 value)
{
    for (i32 idx = 0; idx < numNames; idx++)
    {
        if (names[idx].value == value)
        {
            return names[idx].name;
        }
    }

    return "?";
}

// A state change that the Supervisor hasn't acted upon yet, such as the switch to the next stage.
static bool IsStateChangePending()
{
    return g_Supervisor.wantedState != g_Supervisor.curState;
}

static bool IsInGame()
{
    return !IsStateChangePending() && g_Supervisor.curState == SUPERVISOR_STATE_GAMEMANAGER;
}

static void RedrawGuiCounters()
{
    g_Gui.flags.flag0 = 2;
    g_Gui.flags.flag1 = 2;
    g_Gui.flags.flag2 = 2;
    g_Gui.flags.flag3 = 2;
    g_Gui.flags.flag4 = 2;
}

// Shared by the commands that read or write a single number of the current run.
static bool ParseGameValue(i32 argc, char **argv, i32 current, i32 max, i32 *out)
{
    if (!IsInGame())
    {
        PrintError("%s: only works while in a stage", argv[0]);
        return false;
    }
    if (argc < 2)
    {
        Print("%s is %d", argv[0], current);
        return false;
    }
    if (!ParseInt(argv[1], out) || *out < 0 || *out > max)
    {
        PrintError("%s: expected a number from 0 to %d", argv[0], max);
        return false;
    }

    return true;
}

static void CmdLives(i32 argc, char **argv)
{
    i32 value;

    if (ParseGameValue(argc, argv, g_GameManager.livesRemaining, MAX_LIVES, &value))
    {
        g_GameManager.livesRemaining = value;
        RedrawGuiCounters();
        Print("lives set to %d", value);
    }
}

static void CmdBombs(i32 argc, char **argv)
{
    i32 value;

    if (ParseGameValue(argc, argv, g_GameManager.bombsRemaining, MAX_BOMBS, &value))
    {
        g_GameManager.bombsRemaining = value;
        RedrawGuiCounters();
        Print("bombs set to %d", value);
    }
}

static void CmdPower(i32 argc, char **argv)
{
    i32 value;

    if (ParseGameValue(argc, argv, g_GameManager.currentPower, MAX_POWER, &value))
    {
        g_GameManager.currentPower = value;
        RedrawGuiCounters();
        Print("power set to %d", value);
    }
}

static void CmdGod(i32 argc, char **argv)
{
    (void)argc;
    (void)argv;

    g_GodMode = !g_GodMode;
    Print("god mode %s", g_GodMode ? "on" : "off");
}

static void CmdHitbox(i32 argc, char **argv)
{
    (void)argc;
    (void)argv;

    g_ShowBatHitbox = !g_ShowBatHitbox;
    Print("bat hitbox display %s", g_ShowBatHitbox ? "on" : "off");
}

static const EclTimelineInstr *NextTimelineInstr(const EclTimelineInstr *instr)
{
    return (const EclTimelineInstr *)(((const u8 *)instr) + instr->size);
}

// Removes every enemy and bullet without handing out score or items, bosses and their spellcards included.
static void ClearEnemies()
{
    for (i32 idx = 0; idx < ARRAY_SIZE_SIGNED(g_EnemyManager.enemies) - 1; idx++)
    {
        Enemy *enemy = &g_EnemyManager.enemies[idx];

        if (enemy->flags.active)
        {
            enemy->Despawn();
            // Despawn only hides bosses, which would leave the timeline waiting for them to die.
            enemy->flags.active = 0;
        }
    }

    if (g_EnemyManager.spellcardInfo.isActive)
    {
        g_Gui.EndEnemySpellcard();
        g_EnemyManager.spellcardInfo.isActive = 0;
        g_EnemyManager.spellcardInfo.isCapturing = 0;
    }
    g_Stage.spellcardState = NOT_RUNNING;
    g_Gui.bossPresent = false;
    g_BulletManager.RemoveAllBullets(false);
}

static void CmdSkip(i32 argc, char **argv)
{
    const EclTimelineInstr *current;
    const EclTimelineInstr *cursor;
    const EclTimelineInstr *dialogue;
    const EclTimelineInstr *resumeFrom;

    (void)argc;
    (void)argv;

    if (!IsInGame())
    {
        PrintError("skip: only works while in a stage");
        return;
    }

    current = g_EnemyManager.timelineInstr != NULL ? g_EnemyManager.timelineInstr : g_EclManager.timeline;

    dialogue = NULL;
    for (cursor = current; cursor->time >= 0; cursor = NextTimelineInstr(cursor))
    {
        if (cursor->opCode == TIMELINE_OPCODE_DIALOGUE)
        {
            dialogue = cursor;
            break;
        }
    }

    ClearEnemies();
    SetOpen(false);

    if (dialogue == NULL)
    {
        Gui::EndStage();
        Print("skip: no dialogue left, ending the stage");
        return;
    }

    // The timeline normally resumes at the dialogue itself, but enemies spawned right before it are kept: some
    // bosses show up ahead of their dialogue, and the stage expects them to be there afterwards.
    resumeFrom = NULL;
    for (cursor = current; cursor != dialogue; cursor = NextTimelineInstr(cursor))
    {
        if (cursor->opCode > TIMELINE_OPCODE_LAST_SPAWN)
        {
            resumeFrom = NULL;
        }
        else if (resumeFrom == NULL && cursor->time + SKIP_LEAD_IN_FRAMES >= dialogue->time)
        {
            resumeFrom = cursor;
        }
    }
    if (resumeFrom == NULL)
    {
        resumeFrom = dialogue;
    }
    g_EnemyManager.timelineInstr = resumeFrom;
    g_EnemyManager.timelineTime.SetCurrent(resumeFrom->time);
    Print("skip: jumped to the next dialogue");
}

static void CmdMap(i32 argc, char **argv)
{
    i32 stage;
    i32 character;
    i32 shotType;
    i32 difficulty;
    bool hasShotType;
    bool hasDifficulty;
    i32 idx;

    if (argc < 2 || !ParseInt(argv[1], &stage) || stage < 1 || stage > EXTRA_STAGE + 1)
    {
        PrintError("map: expected a stage from 1 to %d", EXTRA_STAGE + 1);
        return;
    }

    character = g_GameManager.character;
    shotType = g_GameManager.shotType;
    difficulty = g_GameManager.difficulty;
    hasShotType = false;
    hasDifficulty = false;

    for (idx = 2; idx < argc; idx += 2)
    {
        const char *option = argv[idx];

        if (idx + 1 >= argc)
        {
            PrintError("map: %s needs a value", option);
            return;
        }

        const char *value = argv[idx + 1];

        if (std::strcmp(option, "-character") == 0 || std::strcmp(option, "-c") == 0)
        {
            if (!ParseName(value, g_CharacterNames, ARRAY_SIZE_SIGNED(g_CharacterNames), &character))
            {
                PrintError("map: unknown character '%s'", value);
                return;
            }
        }
        else if (std::strcmp(option, "-shot") == 0 || std::strcmp(option, "-s") == 0)
        {
            if (!ParseName(value, g_ShotTypeNames, ARRAY_SIZE_SIGNED(g_ShotTypeNames), &shotType))
            {
                PrintError("map: unknown shot type '%s'", value);
                return;
            }
            hasShotType = true;
        }
        else if (std::strcmp(option, "-difficulty") == 0 || std::strcmp(option, "-d") == 0)
        {
            if (!ParseName(value, g_DifficultyNames, ARRAY_SIZE_SIGNED(g_DifficultyNames), &difficulty))
            {
                PrintError("map: unknown difficulty '%s'", value);
                return;
            }
            hasDifficulty = true;
        }
        else
        {
            PrintError("map: unknown option '%s'", option);
            return;
        }
    }

    // Not every character has both shot types.
    if (character * 2 + shotType >= ARRAY_SIZE_SIGNED(g_BombData))
    {
        if (hasShotType)
        {
            PrintError("map: %s has no shot type %s",
                       NameOf(g_CharacterNames, ARRAY_SIZE_SIGNED(g_CharacterNames), character),
                       NameOf(g_ShotTypeNames, ARRAY_SIZE_SIGNED(g_ShotTypeNames), shotType));
            return;
        }
        shotType = SHOT_TYPE_A;
    }

    // The extra stage and the extra difficulty only exist together.
    if (stage == EXTRA_STAGE + 1)
    {
        difficulty = EXTRA;
    }
    else if (difficulty >= EXTRA)
    {
        if (hasDifficulty)
        {
            PrintError("map: the extra difficulty only exists on stage %d", EXTRA_STAGE + 1);
            return;
        }
        difficulty = g_Supervisor.cfg.defaultDifficulty < EXTRA ? g_Supervisor.cfg.defaultDifficulty : NORMAL;
    }

    if (IsStateChangePending())
    {
        PrintError("map: the game is busy switching screens, try again");
        return;
    }

    // Tear down whatever is running, the same way the Supervisor would.
    switch (g_Supervisor.curState)
    {
    case SUPERVISOR_STATE_GAMEMANAGER:
        GameManager::CutChain();
        ReplayManager::SaveReplay(NULL, NULL);
        break;
    case SUPERVISOR_STATE_MAINMENU:
        g_Chain.Cut(g_MainMenu.chainCalc);
        g_MainMenu.chainCalc = NULL;
        g_Supervisor.StopAudio();
        break;
    default:
        PrintError("map: only works from the title screen or in a stage");
        return;
    }

    g_GameManager.character = character;
    g_GameManager.shotType = shotType;
    g_GameManager.difficulty = (Difficulty)difficulty;
    // GameManager::AddedCallback moves on to the next stage, so this is the one before the stage we want.
    g_GameManager.currentStage = stage - 1;
    g_GameManager.livesRemaining = g_Supervisor.cfg.lifeCount;
    g_GameManager.bombsRemaining = g_Supervisor.cfg.bombCount;
    if (difficulty == EXTRA)
    {
        g_GameManager.livesRemaining = 2;
        g_GameManager.bombsRemaining = 3;
    }
    g_GameManager.isInReplay = 0;
    g_GameManager.isInPracticeMode = 0;
    g_GameManager.demoMode = 0;
    g_GameManager.demoFrames = 0;

    g_Supervisor.wantedState = SUPERVISOR_STATE_GAMEMANAGER;
    g_Supervisor.curState = SUPERVISOR_STATE_GAMEMANAGER;
    if (GameManager::RegisterChain() != ZUN_SUCCESS)
    {
        // Have the Supervisor clean up and bring us back to the title screen.
        g_Supervisor.curState = SUPERVISOR_STATE_MAINMENU;
        PrintError("map: failed to load stage %d", stage);
        return;
    }

    Print("map: stage %d as %s %s on %s", stage,
          NameOf(g_CharacterNames, ARRAY_SIZE_SIGNED(g_CharacterNames), character),
          NameOf(g_ShotTypeNames, ARRAY_SIZE_SIGNED(g_ShotTypeNames), shotType),
          NameOf(g_DifficultyNames, ARRAY_SIZE_SIGNED(g_DifficultyNames), difficulty));
    SetOpen(false);
}

static void CmdClear(i32 argc, char **argv)
{
    (void)argc;
    (void)argv;

    std::memset(g_Log, 0, sizeof(g_Log));
}

static void CmdHelp(i32 argc, char **argv);

// To add a command, write a Cmd function above and list it here.
static const ConsoleCommand g_Commands[] = {
    {"help", "help", CmdHelp},
    {"map", "map <1-7> [-character c] [-shot a|b] [-difficulty d]", CmdMap},
    {"skip", "skip", CmdSkip},
    {"lives", "lives [0-8]", CmdLives},
    {"bombs", "bombs [0-8]", CmdBombs},
    {"power", "power [0-128]", CmdPower},
    {"god", "god", CmdGod},
    {"hitbox", "hitbox", CmdHitbox},
    {"clear", "clear", CmdClear},
};

static void CmdHelp(i32 argc, char **argv)
{
    (void)argc;
    (void)argv;

    for (i32 idx = 0; idx < ARRAY_SIZE_SIGNED(g_Commands); idx++)
    {
        Print("%s", g_Commands[idx].usage);
    }
    Print("characters: reimu, marisa, poyo (or 0-2)");
    Print("difficulties: easy, normal, hard, lunatic, extra (or 0-4)");
}

static void Execute(const char *commandLine)
{
    char buffer[CONSOLE_INPUT_MAX + 1];
    char *argv[CONSOLE_MAX_ARGS];
    i32 argc;
    char *cursor;
    i32 idx;

    std::strcpy(buffer, commandLine);

    // Lowercases the line and splits it on spaces.
    argc = 0;
    cursor = buffer;
    while (argc < CONSOLE_MAX_ARGS)
    {
        while (*cursor == ' ')
        {
            cursor++;
        }
        if (*cursor == '\0')
        {
            break;
        }

        argv[argc++] = cursor;
        while (*cursor != ' ' && *cursor != '\0')
        {
            if (*cursor >= 'A' && *cursor <= 'Z')
            {
                *cursor += 'a' - 'A';
            }
            cursor++;
        }
        if (*cursor != '\0')
        {
            *cursor++ = '\0';
        }
    }

    if (argc == 0)
    {
        return;
    }

    for (idx = 0; idx < ARRAY_SIZE_SIGNED(g_Commands); idx++)
    {
        if (std::strcmp(argv[0], g_Commands[idx].name) == 0)
        {
            g_Commands[idx].run(argc, argv);
            return;
        }
    }

    PrintError("unknown command '%s', try 'help'", argv[0]);
}

static void SubmitInput()
{
    if (g_InputLength == 0)
    {
        return;
    }

    if (g_HistoryCount == CONSOLE_HISTORY_LINES)
    {
        std::memmove(&g_History[0], &g_History[1], sizeof(g_History) - sizeof(g_History[0]));
        g_HistoryCount--;
    }
    std::strcpy(g_History[g_HistoryCount++], g_Input);
    g_HistoryCursor = g_HistoryCount;

    char commandLine[CONSOLE_INPUT_MAX + 1];
    std::strcpy(commandLine, g_Input);
    g_Input[0] = '\0';
    g_InputLength = 0;

    AddLogLine(CONSOLE_PROMPT, sizeof(CONSOLE_PROMPT) - 1, CONSOLE_COLOR_ECHO);
    std::strcat(g_Log[CONSOLE_LOG_LINES - 1].text, commandLine);

    Execute(commandLine);
}

static void BrowseHistory(i32 direction)
{
    i32 cursor = g_HistoryCursor + direction;

    if (cursor < 0 || cursor > g_HistoryCount)
    {
        return;
    }

    g_HistoryCursor = cursor;
    if (cursor == g_HistoryCount)
    {
        g_Input[0] = '\0';
    }
    else
    {
        std::strcpy(g_Input, g_History[cursor]);
    }
    g_InputLength = std::strlen(g_Input);
}

bool DebugConsole::HandleEvent(const SDL_Event *event)
{
    const char *text;

    switch (event->type)
    {
    case SDL_KEYDOWN:
        if (event->key.keysym.scancode == SDL_SCANCODE_GRAVE)
        {
            if (!event->key.repeat)
            {
                SetOpen(!g_IsOpen);
            }
            return true;
        }
        if (!g_IsOpen)
        {
            return false;
        }

        switch (event->key.keysym.sym)
        {
        case SDLK_RETURN:
        case SDLK_KP_ENTER:
            SubmitInput();
            break;
        case SDLK_BACKSPACE:
            if (g_InputLength > 0)
            {
                g_Input[--g_InputLength] = '\0';
            }
            break;
        case SDLK_UP:
            BrowseHistory(-1);
            break;
        case SDLK_DOWN:
            BrowseHistory(1);
            break;
        case SDLK_ESCAPE:
            SetOpen(false);
            break;
        }
        return true;

    case SDL_TEXTINPUT:
        if (!g_IsOpen)
        {
            return false;
        }

        // The ascii font only covers printable ASCII. The key that toggles the console also ends up here.
        for (text = event->text.text; *text != '\0'; text++)
        {
            if (*text >= ' ' && *text <= '~' && *text != '`' && *text != '~' && g_InputLength < CONSOLE_INPUT_MAX)
            {
                g_Input[g_InputLength++] = *text;
                g_Input[g_InputLength] = '\0';
            }
        }
        return true;
    }

    return false;
}

bool DebugConsole::IsOpen()
{
    return g_IsOpen;
}

bool DebugConsole::IsGodModeEnabled()
{
    return g_GodMode;
}

static ChainCallbackResult OnUpdate(void *arg)
{
    (void)arg;

    // Everything that runs after the Supervisor is frozen while the console is open, the same way the pause menu
    // freezes the stage. This also keeps what's being typed from reaching the game.
    if (g_IsOpen)
    {
        return CHAIN_CALLBACK_RESULT_BREAK;
    }

    return CHAIN_CALLBACK_RESULT_CONTINUE;
}

static void SetFullWindowViewport()
{
    g_AnmManager->FlushVertexBuffer();
    g_Supervisor.viewport.x = 0;
    g_Supervisor.viewport.y = 0;
    g_Supervisor.viewport.width = GAME_WINDOW_WIDTH;
    g_Supervisor.viewport.height = GAME_WINDOW_HEIGHT;
    g_AnmManager->SetProjectionMode(PROJECTION_MODE_PERSPECTIVE);
    g_Supervisor.viewport.Set();
}

// Shows the area poyo's bat hits, for as long as a swing is active.
static void DrawBatHitbox()
{
    ZunRect rect;
    f32 regionLeft;
    f32 regionTop;

    if (!IsInGame() || g_GameManager.character != CHARA_POYO || g_Player.reflectionActiveTimer.AsFrames() <= 0)
    {
        return;
    }

    // The player lives in playfield coordinates, DrawSquare wants window coordinates.
    regionLeft = g_GameManager.arcadeRegionTopLeftPos.x;
    regionTop = g_GameManager.arcadeRegionTopLeftPos.y;
    rect.left = regionLeft + g_Player.reflectionTopLeft.x;
    rect.top = regionTop + g_Player.reflectionTopLeft.y;
    rect.right = regionLeft + g_Player.reflectionBottomRight.x;
    rect.bottom = regionTop + g_Player.reflectionBottomRight.y;

    // Keeps the box from spilling over the sidebar when swinging at the edge of the playfield.
    if (rect.left < regionLeft)
    {
        rect.left = regionLeft;
    }
    if (rect.top < regionTop)
    {
        rect.top = regionTop;
    }
    if (rect.right > regionLeft + g_GameManager.arcadeRegionSize.x)
    {
        rect.right = regionLeft + g_GameManager.arcadeRegionSize.x;
    }
    if (rect.bottom > regionTop + g_GameManager.arcadeRegionSize.y)
    {
        rect.bottom = regionTop + g_GameManager.arcadeRegionSize.y;
    }

    SetFullWindowViewport();
    ScreenEffect::DrawSquare(&rect, CONSOLE_COLOR_BAT_HITBOX);
}

static ChainCallbackResult OnDraw(void *arg)
{
    ZunRect rect;
    ZunVec3 pos;
    char inputLine[CONSOLE_COLUMNS + 1];
    u32 time;
    f32 slideStep;
    f32 top;
    i32 idx;

    (void)arg;

    if (g_ShowBatHitbox)
    {
        DrawBatHitbox();
    }

    // Timed off the clock rather than off frames, since the calc chain doesn't run while the console is open.
    time = SDL_GetTicks();
    slideStep = (time - g_LastDrawTime) / CONSOLE_SLIDE_MS;
    g_LastDrawTime = time;
    if (g_IsOpen)
    {
        g_SlideProgress = g_SlideProgress + slideStep > 1.0f ? 1.0f : g_SlideProgress + slideStep;
    }
    else
    {
        g_SlideProgress = g_SlideProgress - slideStep < 0.0f ? 0.0f : g_SlideProgress - slideStep;
    }
    if (g_SlideProgress <= 0.0f)
    {
        return CHAIN_CALLBACK_RESULT_CONTINUE;
    }

    top = (g_SlideProgress - 1.0f) * CONSOLE_HEIGHT;

    SetFullWindowViewport();

    rect.left = 0.0f;
    rect.right = GAME_WINDOW_WIDTH;
    rect.top = top;
    rect.bottom = top + CONSOLE_HEIGHT;
    ScreenEffect::DrawSquare(&rect, CONSOLE_COLOR_BACKGROUND);
    rect.top = rect.bottom;
    rect.bottom = rect.top + 2.0f;
    ScreenEffect::DrawSquare(&rect, CONSOLE_COLOR_BORDER);

    // The text itself is drawn by the AsciiManager, which runs right after us in the draw chain.
    AsciiManager *ascii = &g_AsciiManager;
    ZunColor prevColor = ascii->color;
    ZunVec2 prevScale = ascii->scale;
    u32 prevIsGui = ascii->isGui;
    bool prevIsSelected = ascii->isSelected;

    ascii->scale.x = CONSOLE_TEXT_SCALE;
    ascii->scale.y = CONSOLE_TEXT_SCALE;
    ascii->isGui = 0;
    ascii->isSelected = false;

    pos.x = CONSOLE_PADDING;
    pos.y = top + CONSOLE_PADDING;
    pos.z = 0.0f;
    for (idx = 0; idx < CONSOLE_LOG_LINES; idx++, pos.y += CONSOLE_LINE_HEIGHT)
    {
        if (g_Log[idx].text[0] != '\0')
        {
            ascii->SetColor(g_Log[idx].color);
            ascii->AddString(&pos, g_Log[idx].text);
        }
    }

    std::snprintf(inputLine, sizeof(inputLine), CONSOLE_PROMPT "%s%s", g_Input, time / 400 % 2 == 0 ? "_" : "");
    ascii->SetColor(CONSOLE_COLOR_ECHO);
    ascii->AddString(&pos, inputLine);

    ascii->color = prevColor;
    ascii->scale = prevScale;
    ascii->isGui = prevIsGui;
    ascii->isSelected = prevIsSelected;

    return CHAIN_CALLBACK_RESULT_CONTINUE;
}

ZunResult DebugConsole::RegisterChain()
{
    g_IsOpen = false;
    g_SlideProgress = 0.0f;

    // Both of these share the Supervisor's priority, which puts them right after it: the calc callback runs once
    // inputs are read but before anything acts on them, and the draw callback runs on top of the rest of the game.
    g_DebugConsoleCalcChain.callback = (ChainCallback)OnUpdate;
    g_DebugConsoleCalcChain.addedCallback = NULL;
    g_DebugConsoleCalcChain.deletedCallback = NULL;
    g_DebugConsoleCalcChain.arg = NULL;
    if (g_Chain.AddToCalcChain(&g_DebugConsoleCalcChain, TH_CHAIN_PRIO_CALC_SUPERVISOR) != 0)
    {
        return ZUN_ERROR;
    }

    g_DebugConsoleDrawChain.callback = (ChainCallback)OnDraw;
    g_DebugConsoleDrawChain.addedCallback = NULL;
    g_DebugConsoleDrawChain.deletedCallback = NULL;
    g_DebugConsoleDrawChain.arg = NULL;
    g_Chain.AddToDrawChain(&g_DebugConsoleDrawChain, TH_CHAIN_PRIO_DRAW_SUPERVISOR);

    return ZUN_SUCCESS;
}

#endif
