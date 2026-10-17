@echo off
pip install pywebview pyinstaller
pyinstaller --onefile --windowed --name SpeziFinder --add-data "index.html;." app.py
echo.
echo Fertig: dist\SpeziFinder.exe
pause
