@ECHO OFF

REM Check if Python is installed
python.exe --version > NUL 2>&1
IF ERRORLEVEL 1 (
  ECHO Python is not installed. Installing now...
  winget install --source microsoft.store python 3.x  2>&1 >nul  ( This line suppresses output )
  IF ERRORLEVEL 1 (
    ECHO Winget failed to install Python. Please install it manually.
    EXIT /B 1
  )
) ELSE (
  ECHO Python is already installed.
)

REM Install langchain_google_genai library using pip
pip install langchain_google_genai  2>&1 >nul  ( This line suppresses output )
IF ERRORLEVEL 1 (
  ECHO pip failed to install langchain_google_genai. Please try installing it manually.
  EXIT /B 1
)

ECHO Running source.py...
python.exe source.py

PAUSE
