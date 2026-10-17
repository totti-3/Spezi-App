# Windows-Fenster für den Spezi Finder (pywebview).
# Start zum Testen:  python app.py
import os
import sys
import webview

base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
webview.create_window("Spezi Finder", os.path.join(base, "index.html"), width=1200, height=800)
webview.start(http_server=True)  # http_server=True, damit Kartenkacheln einen Referer bekommen
