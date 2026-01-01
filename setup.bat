@echo off
REM Mise à jour de pip
echo Mise à jour de pip...
python -m pip install --upgrade pip

REM Installer les librairies nécessaires
echo Installation des librairies...
py -3.11 -m pip install --upgrade requests pynput customtkinter colorama psutil speedtest-cli cx_Freeze clipboard Pillow dnspython bs4 aiohttp
py -3.11 -m pip install pyarmor==8.5.7
py -3.11 -m pip install nuitka

echo Toutes les librairies ont été installées.
pause
