@echo off
py -3.12 -m venv .venv
call .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
pause
