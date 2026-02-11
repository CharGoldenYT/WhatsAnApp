import webview as wv

import src.back.utils.print as print
import src.back.system.settings as settings

settings.checkIfExist()

def startUp(debugWaa=False, debugYes=False):
    print.success("Flask and PyWebView is starting! Please wait...")
    if debugWaa:
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

    wv.create_window(
        'WhatsAnApp - A better native whatsapp expirence.',
        'https://example.com',
        width=1280,
        height=720
    )
    # waaWindow.events.loaded += lambda: injections(waaWindow)

    wv.start(
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        storage_path = settings.fullAppConfig + "Chromium Storage",
        private_mode=False,

        # Debugging purposes.
        debug=debugYes
    )
