# Touhou 6: Embodiment of Scarlet Devil - Poyo Mod
This mod adds a third character to the game named Poyo.

This can serve as an example on how to also make your own characters!

Once you compile this, drag and drop the poyo.DAT into the same folder as your Touhou game data. Once you launch the custom .exe file, this should work just fine.

## HEADS UP!!

This project uses AI-generated build tools and debugging tools for ease of convenience, but has been reviewed to ensure none of it conflicts with gameplay.

However, the ACTUAL code (the character, mechanics, etc) has been mostly human-made, but AI-assisted (fixing bugs and whatnot). I know you guys have a really strong stance on AI, but I am still new to the Touhou codebase, let alone coding with C as a whole (I code in HaxeFlixel and Lua). I want to make a good mod with my friends to innovate around the scene, but I wasn't sure if I knew anyone that both wanted to help with the project coding-wise. All AI code has been reviewed to ensure it's safe and not able to conflict with the game itself.

## Building the Poyo assets

Run `build-dat.bat` to compile every `.spec` file in `poyo-assets\spec-files` to a matching `.anm` and every `.msg` file to a matching `.dat`. The generated files replace their counterparts in `poyo-assets\assets`; the script then packs the assets into `obj\poyo.DAT` and copies it to `game\poyo.DAT`.

Position sources named `NAME.pos.txt` in `poyo-assets\spec-files` are also compiled to `NAME.pos`. They contain two times in milliseconds (decimals are allowed): loop start, then loop end (exclusive); for example, `1000` is 1 second and `1200` is 1.2 seconds. The build converts milliseconds to the WAV's 44,100 Hz sample frames and checks that the loop fits the corresponding `NAME.wav` before packing. `tools\compile-pos.ps1` can also decompile a binary `.pos` file to millisecond text.

The script expects `truanm.exe`, `trumsg.exe`, `thdat.exe`, and the Touhou 6 maps `th06.anmm` and `th06.msgm` under `C:\DevTools` and `C:\DevTools\TouhouMaps-main`, respectively. Compiling `.pos.txt` sources requires Windows PowerShell.

# TH06 Portable Decomp README
[![Discord][discord-badge]][discord] <- click here to join discord server.

[discord]: https://discord.gg/VyGwAjrh9a
[discord-badge]: https://img.shields.io/discord/1147558514840064030?color=%237289DA&logo=discord&logoColor=%23FFFFFF

This is the readme for the portable fork of EoSD. For the readme of the decomp project, see [here](https://github.com/GensokyoClub/th06/blob/master/README.md).

EoSD-portable is a port of Touhou 6 using SDL2 and OpenGL (with a more general renderer abstraction layer hopefully on the way).
This enables theoretical portability to any system supported by SDL2, with Linux, Windows, and macOS in particular being known to work.
Builds for the BSDs and other Unices are also almost certainly possible, but may require some slight modifications to the build system.

### Platform Requirements

- SDL2, SDL2-image, and SDL2-ttf support
- C++20 standard library support
- A little endian architecture (though big endian support is currently being worked on)
- OpenGL ES 1.1, OpenGL 1.3, or GL 2.1 / GL ES 2.0 / WebGL support

### Dependencies

EoSD-portable has the following dependencies:

- `SDL2`
- `SDL2_image`
- `SDL2_ttf`
- `libasound` (Optional and Linux-only, enables MIDI support. This will almost always be present as part of a desktop distro.)

On Windows and macOS, MIDI support uses the system APIs and needs no extra dependencies.

In addition, building uses [`premake5`](https://premake.github.io/download) and a compiler that supports C++20.

#### Building

In the repository root directory, run `premake5` with the desired build system as an argument (a list can be seen by running `premake5 --help`).
This will output the build files to the `build` directory, and then compilation may be done with the desired build system.

##### Build Options (Use with Premake Invocation)
`--no-asoundlib`: On Linux, doesn't build MIDI support. Removes libasound as a dev and runtime dependency

`--use-c23-embed`: Uses `#embed` for resource inclusion instead of a lua script in the Premake file.

`--no-debug-console`[FROM POYO!!]: Builds without the in-game debug console (opened with the `` ` `` key, type `help` for a list of commands).

##### Build Example (Debian-based Linux)

Obtain dependencies:

`sudo apt install build-essential libsdl2-dev libsdl2-image-dev libsdl2-ttf-dev libasound2-dev`

Generate makefile:

`premake5 gmake`

Compile:

`cd build && make -j16`

##### Build Example (macOS)

Install the Xcode Command Line Tools (provides the compiler), if not already present:

`xcode-select --install`

Obtain dependencies (using [Homebrew](https://brew.sh)):

`brew install premake sdl2 sdl2_image sdl2_ttf`

Generate makefile:

`premake5 gmake`

Compile:

`cd build && make -j16`

### Use

EoSD-portable is designed to be a drop-in replacement for the vanilla EoSD binary.
You will also need to add a font to your game directory with the filename `msgothic.ttc`.
This may be the actual MS Gothic, taken from a Windows machine, or a compatible font such as Kochi Gothic.
EoSD-portable uses the Japanese filenames (e.g. 紅魔郷CM.DAT, 東方紅魔郷.cfg). English and other patches, static or thcrap, do not currently work.
A Japanese locale is not required.

# Decomp Credits

We would like to extend our thanks to the following individuals for their
invaluable contributions:

- @EstexNT for porting the [`var_order` pragma](scripts/pragma_var_order.cpp) to
  MSVC7.
