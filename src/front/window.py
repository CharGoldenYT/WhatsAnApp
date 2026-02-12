import os
import sys
import threading
import time

import webview as wv

import src.back.system.settings as settings
import src.back.utils.print as print

def startUp(debugMode=False):
    settings.checkIfExist()
    print.success("Flask and PyWebView is starting! Please wait...")

    projectRoot = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    if debugMode:
        print.debug("From now on, below this print, PyWebView's logging.")

    wv.create_window(
        "WhatsAnApp",
        "https://web.whatsapp.com/",
        width=1280,
        height=720,
    )

    if not sys.platform == "win32":
        iconPath = os.path.join(projectRoot, "assets", "WhatsAnApp.png")
    else:
        iconPath = os.path.join(projectRoot, "assets", "WhatsAnApp.ico")
    print.debug(f"Using icon PyWebView icon at: {iconPath}")

    wv.start(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        storage_path=settings.fullAppConfig + "Chromium Storage",
        private_mode=False,
        icon=iconPath,
        
        # Debugging purposes.
        debug=debugMode,
    )
