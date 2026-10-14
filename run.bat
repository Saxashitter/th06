@echo off
rem Copies th06.exe and poyo.DAT into game\ and launches the game from there.
setlocal
set ROOT=%~dp0
set GAME=%ROOT%game
if not exist "%GAME%\th06.exe" (
    echo th06.exe not found - run build.bat first.
    exit /b 1
)
if not exist "%GAME%\poyo.DAT" (
    echo poyo.DAT not found - run build-dat.bat first.
    exit /b 1
)

pushd "%GAME%"
th06.exe > "%ROOT%game.log" 2>&1
popd