import os
import sys
import json

import src.back.utils.print as print

appID = "app.netlify.daveberry.WhatsAnApp"
appConfig = ""
def getOS():
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
    return appConfig

fullAppConfig = getOS() + appID + "/"
def checkIfExist():
    if not os.path.exists(fullAppConfig):
        print.warning(f"App config not found. Creating one at [{fullAppConfig}]...")
        os.makedirs(fullAppConfig)

        os.makedirs(fullAppConfig + "Chromium Storage")
        with open(fullAppConfig + "Chromium Storage/DO NOT SHARE THIS FOLDER. INCLUDING THE OFFICAL DEVS!!!", "w") as f:
            f.write("")
    else:
        print.success(f"App config found! Using [{fullAppConfig}]")
        pass