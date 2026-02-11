import webview as wv
import sys
import os

import src.back.system.settings as settings
import src.back.utils.print as print

def startUp(debugMode=False):
    settings.checkIfExist()
    print.success("Flask and PyWebView is starting! Please wait...")
    if debugMode:
        print.info("From now on, below this print, PyWebView's logging.")
        # whereCSS = "assets/style.css"
        # whereJS = "assets/script.js"

        # def injections(w):
        #     if os.path.exists(whereCSS):
        #         with open(whereCSS, "r") as f:
        #             w.load_css(f.read())
        #     if os.path.exists(whereJS):
        #         with open(whereJS, "r") as f:
        #             w.evaluate_js(f.read())

    wv.create_window("WhatsAnApp", "https://example.com/", width=1280, height=720)
    # waaWindow.events.loaded += lambda: injections(waaWindow)

    projectRoot = os.path.dirname(os.path.abspath(__file__))
    if not sys.platform == "win32":
        iconPath = os.path.join(projectRoot, "assets", "WhatsAnApp.png")
    else:
        iconPath = os.path.join(projectRoot, "assets", "WhatsAnApp.ico")

    wv.start(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        storage_path=settings.fullAppConfig + "Chromium Storage",
        private_mode=False,
        icon=iconPath,
        
        # Debugging purposes.
        debug=debugMode,
    )
