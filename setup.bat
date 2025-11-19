@echo off
REM Vérifie si Python est installé
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python n'est pas installé. Veuillez l'installer d'abord. avec le PATH.exe !!
    pause
    exit /b
)

REM Mettre à jour pip
echo Mise à jour de pip...
echo 

python -m pip install --upgrade pip

REM Installer les librairies nécessaires
echo Installation des librairies...
python -m pip install requests
python -m pip install pynput
python -m pip install customtkinter
python -m pip install colorama
python -m pip install psutil
python -m pip install speedtest-cli


echo Toutes les librairies ont été installées.
pause
