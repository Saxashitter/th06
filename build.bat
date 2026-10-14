@echo off
rem Builds th06.exe (Release) and moves it into game\, replacing the old one.
rem Run from a Developer Command Prompt.
setlocal

where msbuild >nul 2>&1 || (
    echo msbuild not found - run this from the Developer Command Prompt.
    exit /b 1
)

cd /d "%~dp0build"
msbuild th06.vcxproj /p:Configuration=Release /m /nologo /v:minimal || exit /b 1

move /y "%~dp0th06.exe" "%~dp0game\" >nul || (
    echo Couldn't move th06.exe into game\ - is the game still running?
    exit /b 1
)
echo Moved to game\th06.exe
exit /b 0
