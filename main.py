import flask as fl
import webview as wv
import os
import sys
import threading

# Checking...

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
    print("Could not identify OS! Falling back...")
    appConfig = "~/." # when the library doesn't detect the OS, it'll make a dotfolder instead.

fullAppConfig = appConfig + appID + "/"

print("--------------------------------")
print(f"""WhatsAnApp Infomation:
-> Config path: {fullAppConfig}
-> Operating System: {sys.platform}
--------------------------------""")

if not os.path.exists(fullAppConfig):
    print(f"-> App config not found. Creating one at [{fullAppConfig}]...")
    os.makedirs(fullAppConfig)
    
    os.makedirs(fullAppConfig + "Chromium Storage")
    with open(fullAppConfig + "Chromium Storage/DO NOT SHARE THIS FOLDER. INCLUDING THE OFFICAL DEVS!!!", "w") as f:
        f.write("")
else:
    print(f"-> App config found! Using [{fullAppConfig}]")
    pass

print("--> Flask and PyWebView is starting! Please wait...")
print("")
print("--> From now on, below this line, is Flask and PyWebView's logging.")
print("--------------------------------")

# Flask and WebView initialize

def injections(w):
    if os.path.exists(whereCSS):
        with open(whereCSS, "r") as f:
            w.load_css(f.read())
    if os.path.exists(whereJS):
        with open(whereJS, "r") as f:
            w.evaluate_js(f.read())    

waaWindow = wv.create_window('WhatsAnApp - A WhatsApp UI Modification.', 'https://web.whatsapp.com', width=800, height=600)
waaWindow.events.loaded += lambda: injections(waaWindow)
wv.start(
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    storage_path = fullAppConfig + "Chromium Storage",
    private_mode=False,
    
    # Debugging purposes.
    # debug=True
)

print("--------------------------------")
print("--> App closing. Goodbye World!")