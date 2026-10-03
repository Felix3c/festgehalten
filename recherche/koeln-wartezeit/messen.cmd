@echo off
rem Wrapper fuer die Windows-Aufgabenplanung: fester Python-Pfad, Ausgabe ins Log.
rem Angelegt 11.09.2026. Aufgaben: koeln-wartezeit-mo-1000, -mo-1400, -mi-1000.
rem Seit 03.10.2026: schreibt in messwerte-laptop.csv, uebernommen wird per nachtragen.py.
set PYTHONUTF8=1
set PY=C:\Users\skyla\AppData\Local\Programs\Python\Python312\python.exe
set DIR=%~dp0
echo ==== %DATE% %TIME% ==== >> "%DIR%messen.log"
"%PY%" "%DIR%messen.py" --csv "%DIR%messwerte-laptop.csv" >> "%DIR%messen.log" 2>&1
echo exit=%ERRORLEVEL% >> "%DIR%messen.log"
