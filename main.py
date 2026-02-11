from tkinter.constants import TRUE
import webview as wv
import src.back.utils.print as print
import os
import sys
import argparse

print.info("Starting the app. Please wait...")
# Checking...

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')
args = parser.parse_args()
debugWaa = args.debug

debugYes = ""
if debugWaa:
    debugYes = True
else:
    debugYes = False

if debugWaa:
    print.success("Debug mode enabled! Please be careful with this.")
else:
    print.info("Debug mode isn't enabled. Acting like a regular user.")

appID = "app.netlify.daveberry.WhatsAnApp"
appConfig = ""

whereCSS = "assets/style.css"
whereJS = "assets/script.js"

if sys.platform == "win32":
    appConfig = os.path.expanduser("~\\Appdata\\Roaming\\")
    #                              stupid ass windows
elif sys.platform == "linux":
    appConfig = os.path.expanduser("~/.config/")
elif sys.platform == "darwin":
    appConfig = os.path.expanduser("~/Library/Application Support/")
else:
    print.warning("Could not identify OS! Falling back...")
    appConfig = os.path.expanduser("~/.") # when the library doesn't detect the OS, it'll make a dotfolder in the home folder instead.

fullAppConfig = appConfig + appID + "/"

print.info("WhatsAnApp Infomation:")
print.info(f"-> Config path: {fullAppConfig}")
print.info(f"-> Operating System: {sys.platform}")

if not os.path.exists(fullAppConfig):
    print.warning(f"App config not found. Creating one at [{fullAppConfig}]...")
    os.makedirs(fullAppConfig)
    
    os.makedirs(fullAppConfig + "Chromium Storage")
    with open(fullAppConfig + "Chromium Storage/DO NOT SHARE THIS FOLDER. INCLUDING THE OFFICAL DEVS!!!", "w") as f:
        f.write("")
else:
    print.success(f"App config found! Using [{fullAppConfig}]")
    pass

print.success("Flask and PyWebView is starting! Please wait...")
if debugWaa:
    print.info("From now on, below this print, PyWebView's logging.")

# Flask and WebView initialize

# def injections(w):
#     if os.path.exists(whereCSS):
#         with open(whereCSS, "r") as f:
#             w.load_css(f.read())
#     if os.path.exists(whereJS):
#         with open(whereJS, "r") as f:
#             w.evaluate_js(f.read())    

waaWindow = wv.create_window('WhatsAnApp - A better native whatsapp expirence.', 'https://web.whatsapp.com', width=800, height=600)
# waaWindow.events.loaded += lambda: injections(waaWindow)

wv.start(
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    storage_path = fullAppConfig + "Chromium Storage",
    private_mode=False,
    
    # Debugging purposes.
    debug=debugYes
)

print.success("App closing. Goodbye World!")