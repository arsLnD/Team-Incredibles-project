@echo off
REM Проверка структуры репозитория Team-incredibles-project.
REM Аргументы передаются в scripts\check-structure.py, например --pending.

setlocal
set "ROOT=%~dp0.."

where python >nul 2>&1
if %ERRORLEVEL%==0 (
  python "%ROOT%\scripts\check-structure.py" %*
  exit /b %ERRORLEVEL%
)

where py >nul 2>&1
if %ERRORLEVEL%==0 (
  py -3 "%ROOT%\scripts\check-structure.py" %*
  exit /b %ERRORLEVEL%
)

echo Нужен Python 3, чтобы запустить scripts\check-structure.py.
exit /b 1
