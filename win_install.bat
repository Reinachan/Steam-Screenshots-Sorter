@echo off
title "Installing Python ..."
echo "Installing Python"
winget install "Python 3"

title "Installing Pipenv ..."
echo "Installing required Pipenv which is required to run the project correctly"
pip install pipenv

title "Installing dependencies"
echo "Installing required python module dependencies"
cd /D "%~dp0"
pipenv install

echo "SETUP COMPLETE. You can now run start.bat."
echo "If you got a bunch of errors, you may have to rerun this script as an admin. Right click the file and click run as administrator."
echo "If rerunning as administrator tells you that you've already installed pipenv, try running this command before rerunning as an admin:"
echo "pip uninstall pipenv"