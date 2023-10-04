@echo off

git pull https://github.com/BronOfFireUnkn/SeeleAssistantCode.git

:: Deactivate the virtual environment
call .\Dev-seele\Scripts\deactivate.bat

:: Calling external python program to check for local modules
python .\setup\check_local_modules.py --no_question

:: Activate the virtual environment
call .\Dev-seele\Scripts\activate.bat

py main.py
