import argparse
import sys

import src.back.system.settings as settings
import src.back.utils.print as print
import src.front.window as window
import src.front.windows.settings as wSettings

print.info("Starting the app. Please wait...")

# Starting the app

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true", help="enable debug mode")
parser.add_argument( "-s", "--settings", action="store_true", help="enable settings mode")
args = parser.parse_args()

debugMode = args.debug
settingsMode = args.settings

if debugMode:
    print.success("Debug mode enabled! Please be careful with this.")
else:
    print.info("Debug mode isn't enabled. Acting like a regular user.")

if settingsMode:
    if debugMode:
        print.warning("This is completely unnecessary. (Debug Flag with Settings)")
    
    print.success("Completely skipping WhatsAnApp, and initalizing settings.")
    wSettings.startUp()
else:
    fullAppConfig = settings.getOS() + settings.appID + "/"
    
    print.info("WhatsAnApp Infomation:")
    print.info(f"-> Config path: {fullAppConfig}")
    print.info(f"-> Operating System: {sys.platform}")
    
    window.startUp(debugMode)
    print.success("App closing. Goodbye World!")
