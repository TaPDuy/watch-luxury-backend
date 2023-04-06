@echo off

IF "%~1" == "" (
    %~dp0\..\.venv\Scripts\python.exe %~dp0\..\manage.py test
) ELSE (
    %~dp0\..\.venv\Scripts\python.exe %~dp0\..\manage.py test %*
)
