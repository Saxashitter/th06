#pragma once

// #include <Windows.h>
// #include <d3d8.h>
// #include <d3dx8math.h>

#include "Chain.hpp"
#include "ResultScreen.hpp"
#include "ZunResult.hpp"
#include "inttypes.hpp"

enum Difficulty
{
    EASY,
    NORMAL,
    HARD,
    LUNATIC,
    EXTRA,
};

enum StageNumber
{
    STAGE1,
    STAGE2,
    STAGE3,
    STAGE4,
    STAGE5,
    FINAL_STAGE,
    EXTRA_STAGE,
};

#define PSCR_NUM_CHARS_SHOTTYPES 4
#define PSCR_NUM_STAGES 6
#define PSCR_NUM_DIFFICULTIES 4

#define CLRD_NUM_CHARACTERS 4

#define CATK_NUM_CAPTURES 64

#define GAME_REGION_TOP 16.0
#define GAME_REGION_LEFT 32.0

#define GAME_REGION_WIDTH 384.0
#define GAME_REGION_HEIGHT 448.0

#define GAME_REGION_RIGHT (GAME_REGION_LEFT + GAME_REGION_WIDTH)
#define GAME_REGION_BOTTOM (GAME_REGION_TOP + GAME_REGION_HEIGHT)

#define DEATH_ZOOM_IN_FRAMES 10
#define DEATH_ZOOM_OUT_FRAMES 40
#define DEATH_FREEZE_FRAMES (35 + DEATH_ZOOM_OUT_FRAMES)
// how much closer the camera gets at full zoom (2.2 = 220% scale)
#define DEATH_ZOOM_FACTOR 2.2f

struct GameManager;
struct AnmVm;

extern GameManager g_GameManager;
struct GameManager
{
    GameManager();
    static ZunResult RegisterChain();
    static void CutChain();
    static ChainCallbackResult OnUpdate(GameManager *gameManager);
    static ChainCallbackResult OnDraw(GameManager *gameManager);
    static ZunResult AddedCallback(GameManager *gameManager);
    static ZunResult DeletedCallback(GameManager *gameManager);
    static void SetupCamera(f32);
    static void SetupCameraStageBackground(f32);
    // poyo's death hit-stop: freezes the game and zooms the camera in on the given point
    void StartDeathFreeze(f32 focusX, f32 focusY);
    void UpdateDeathFreeze();
    // For sprites drawn in screen space (which ignore the camera): scale and position that match what the
    // zoomed camera does to something drawn at game-region coords (x, y).
    f32 GetDeathZoomScale() const;
    void ApplyDeathZoomToPoint(f32 *x, f32 *y) const;
    bool IsDeathFrozen() const
    {
        return this->deathFreezeFrames >= (DEATH_FREEZE_FRAMES - DEATH_ZOOM_OUT_FRAMES);
    }

    i32 HasReachedMaxClears(i32 character, i32 shottype) const;
    void IncreaseSubrank(i32 amount);
    void DecreaseSubrank(i32 amount);
    i32 IsInBounds(f32 x, f32 y, f32 width, f32 height) const;

    void AddScore(i32 points)
    {
        this->score += points;
    }

    static i32 CharacterShotType()
    {
        return g_GameManager.shotType + g_GameManager.character * 2;
    }

    u32 guiScore;
    u32 score;
    u32 nextScoreIncrement;
    u32 highScore;
    Difficulty difficulty;
    i32 grazeInStage;
    i32 grazeInTotal;
    u32 isInReplay;
    i32 deaths;
    i32 bombsUsed;
    i32 spellcardsCaptured;
    i8 isTimeStopped;
    // poyo's death hit-stop: while deathFreezeFrames > 0 the game logic is paused and the camera zooms in on
    // (deathZoomX, deathZoomY). deathZoomAmount is the eased 0..1 zoom strength.
    i32 deathFreezeFrames;
    f32 deathZoomAmount;
    f32 deathZoomX;
    f32 deathZoomY;
    Catk catk[CATK_NUM_CAPTURES];
    Clrd clrd[CLRD_NUM_CHARACTERS];
    Pscr pscr[PSCR_NUM_CHARS_SHOTTYPES][PSCR_NUM_STAGES][PSCR_NUM_DIFFICULTIES];
    u16 currentPower;
    i8 unk_1812;
    i8 unk_1813;
    u16 pointItemsCollectedInStage;
    u16 pointItemsCollected;
    u8 numRetries;
    i8 powerItemCountForScore;
    i8 livesRemaining;
    i8 bombsRemaining;
    i8 extraLives;
    u8 character;
    u8 shotType;
    u8 isInGameMenu;
    u8 isInRetryMenu;
    u8 isInMenu;
    u8 isGameCompleted;
    u8 isInPracticeMode;
    u8 demoMode;
    i8 unk_1825;
    i8 unk_1826;
    i8 unk_1827;
    i32 demoFrames;
    i8 replayFile[256];
    i8 unk_192c[256];
    u16 randomSeed;
    u32 gameFrames;
    i32 currentStage;
    u32 menuCursorBackup;
    ZunVec2 arcadeRegionTopLeftPos;
    ZunVec2 arcadeRegionSize;
    ZunVec2 playerMovementAreaTopLeftPos;
    ZunVec2 playerMovementAreaSize;
    f32 cameraDistance;
    ZunVec3 stageCameraFacingDir;
    i32 counat;
    i32 rank;
    i32 maxRank;
    i32 minRank;
    i32 subRank;
};

// For game-world sprites drawn in screen space (they ignore the camera): while this is alive the vm sits where
// the zoomed camera would put it, and is scaled to match. vm->pos must already include arcadeRegionTopLeftPos.
struct DeathZoomedVm
{
    explicit DeathZoomedVm(AnmVm *vm);
    ~DeathZoomedVm();

    AnmVm *vm;
    f32 savedX, savedY, savedScaleX, savedScaleY;
};
