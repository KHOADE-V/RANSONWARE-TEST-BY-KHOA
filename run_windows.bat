@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if not errorlevel 1 (
    py -3 ransomware_sim.py
) else (
    python ransomware_sim.py
)

if errorlevel 1 (
    echo.
    echo Could not start the demo. Check that Python 3 and Tkinter are installed.
    echo Download Python from https://www.python.org/downloads/
    pause
)

endlocal
