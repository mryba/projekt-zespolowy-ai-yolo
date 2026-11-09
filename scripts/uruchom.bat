@echo off
rem Uruchamia notebook projektu (Windows, cmd i PowerShell):
rem tworzy srodowisko .venv, jesli go brak, instaluje zaleznosci i startuje Jupyter.
setlocal
cd /d "%~dp0.."

set PY=python
where python >nul 2>nul
if errorlevel 1 set PY=py -3

if not exist ".venv" (
  echo Tworze srodowisko wirtualne .venv ...
  %PY% -m venv .venv
  if errorlevel 1 goto blad
)

call .venv\Scripts\activate.bat
echo Instaluje zaleznosci ^(pierwsze uruchomienie moze potrwac^) ...
pip install -r requirements.txt
if errorlevel 1 goto blad

echo Uruchamiam notebook ...
jupyter notebook notebooks\projekt_yolo.ipynb
goto koniec

:blad
echo Wystapil blad. Sprawdz, czy jest zainstalowany Python 3.9 lub nowszy.
exit /b 1

:koniec
endlocal
