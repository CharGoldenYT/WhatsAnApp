import argparse
import sys

import src.back.system.settings as settings
import src.back.utils.print as print
import src.front.window as window

print.info("Starting the app. Please wait...")

# Starting the app

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
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

fullAppConfig = settings.getOS() + settings.appID + "/"

print.info("WhatsAnApp Infomation:")
print.info(f"-> Config path: {fullAppConfig}")
print.info(f"-> Operating System: {sys.platform}")

window.startUp(debugWaa, debugYes)
print.success("App closing. Goodbye World!")
