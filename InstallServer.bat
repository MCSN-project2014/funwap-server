@echo off
echo FUNWAP-server 
echo Installation Scripts

rem python _install\get-pip.py

echo.
echo Install python virtualenv
pip install virtualenv

echo.
echo Create a new python enviroment in the current folder
virtualenv venv

echo.
echo Install all the needed library
venv\Scripts\pip install -r requirements.txt

pause
