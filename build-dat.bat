@echo off
rem Compiles every Poyo .spec and .msg file, then packs them together with
rem the rest of poyo-assets\assets into obj\poyo.DAT using thtk's thdat,
rem then replaces game\poyo.DAT with it.
setlocal enabledelayedexpansion

set TOOLS=C:\DevTools
set MAPS=%TOOLS%\TouhouMaps-main
set ROOT=%~dp0
set SPECS=%ROOT%poyo-assets\spec-files
set ASSETS=%ROOT%poyo-assets\assets
set COMPILED=%ROOT%obj\poyo-compiled
set STAGE=%ROOT%obj\poyo-dat
set OUT=%ROOT%obj\poyo.DAT

if not exist "%TOOLS%\truanm.exe" (
    echo truanm.exe not found in %TOOLS%.
    exit /b 1
)
if not exist "%TOOLS%\trumsg.exe" (
    echo trumsg.exe not found in %TOOLS%.
    exit /b 1
)
if not exist "%TOOLS%\thdat.exe" (
    echo thdat.exe not found in %TOOLS%.
    exit /b 1
)
if not exist "%MAPS%\th06.anmm" (
    echo th06.anmm not found in %MAPS%.
    exit /b 1
)
if not exist "%MAPS%\th06.msgm" (
    echo th06.msgm not found in %MAPS%.
    exit /b 1
)
if not exist "%SPECS%\" (
    echo Spec files folder not found: %SPECS%
    exit /b 1
)
if not exist "%ASSETS%\" (
    echo Assets folder not found: %ASSETS%
    exit /b 1
)

if exist "%COMPILED%" rmdir /s /q "%COMPILED%"
mkdir "%COMPILED%" || exit /b 1

rem Compile every spec to a matching .anm and every message to a matching .dat.
for %%F in ("%SPECS%\*.spec") do if exist "%%~fF" (
    echo truanm  %%~nxF
    "%TOOLS%\truanm.exe" compile -g 6 -m "%MAPS%\th06.anmm" "%%~fF" -o "%COMPILED%\%%~nF.anm" || goto :fail
)

for %%F in ("%SPECS%\*.msg") do if exist "%%~fF" (
    echo trumsg  %%~nxF
    "%TOOLS%\trumsg.exe" compile -g 6 -m "%MAPS%\th06.msgm" "%%~fF" -o "%COMPILED%\%%~nF.dat" || goto :fail
)

for %%F in ("%SPECS%\*.pos.txt") do if exist "%%~fF" (
    set "POSNAME=%%~nF"
    set "POSNAME=!POSNAME:.pos=!"
    echo compile %%~nxF
    powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%ROOT%tools\compile-pos.ps1" -Mode compile -Source "%%~fF" -Output "%COMPILED%\!POSNAME!.pos" -Wave "%ASSETS%\!POSNAME!.wav" || goto :fail
)

rem Install generated assets only after all source files compile successfully.
for %%F in ("%COMPILED%\*") do if exist "%%~fF" (
    copy /y "%%~fF" "%ASSETS%\%%~nxF" >nul || goto :fail
)

if exist "%STAGE%" rmdir /s /q "%STAGE%"
mkdir "%STAGE%" || exit /b 1

rem Pack the assets, including the compiled files just installed above.
copy /y "%ASSETS%\*" "%STAGE%" >nul || exit /b 1

rem the game looks entries up by bare filename, so pack from inside the staging folder
if exist "%OUT%" del "%OUT%"
pushd "%STAGE%"
set FILES=
for %%f in (*) do set FILES=!FILES! "%%f"
echo thdat   poyo.DAT
"%TOOLS%\thdat.exe" -c 6 "%OUT%" !FILES!
set RESULT=%errorlevel%
popd
if not "%RESULT%"=="0" goto :fail

echo Built %OUT%

copy /y "%OUT%" "%ROOT%game\" >nul || (
    echo Couldn't copy poyo.DAT into game\ - is the game still running?
    exit /b 1
)
echo Copied to game\poyo.DAT
exit /b 0

:fail
echo DAT build failed.
exit /b 1
