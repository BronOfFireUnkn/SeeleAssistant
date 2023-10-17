@echo off

call .\venv\Scripts\deactivate.bat
python .\setup\check_local_modules.py --no_question
call .\venv\Scripts\activate.bat

py ./Android/main.py

pause