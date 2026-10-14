#pragma once

// Drop-down debug console, toggled with the ` key.
//
// The whole feature only exists when DEBUG_CONSOLE is defined. Premake defines it by default, pass
// --no-debug-console to premake5 to build without it.
#ifdef DEBUG_CONSOLE

#include <SDL2/SDL_events.h>

#include "ZunResult.hpp"

namespace DebugConsole
{
ZunResult RegisterChain();

// Returns true if the console used the event, in which case the game shouldn't see it.
bool HandleEvent(const SDL_Event *event);

bool IsOpen();
bool IsGodModeEnabled();
}; // namespace DebugConsole

#endif
