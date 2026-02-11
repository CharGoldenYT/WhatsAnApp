import customtkinter as ctk
import tkinter as tk
import sys
import os

import src.back.utils.print as print

def startUp():
    window = ctk.CTk()
    window.title("WhatsAnApp - Settings")
    window.geometry("400x600")
    
    assetsPath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'assets')
    if sys.platform == "win32":
        iconPath = os.path.join(assetsPath, 'WhatsAnApp.ico')
        if os.path.exists(iconPath):
            window.iconbitmap(iconPath)
    else:
        iconPath = os.path.join(assetsPath, 'WhatsAnApp.png')
        if os.path.exists(iconPath):
            window.iconphoto(False, tk.PhotoImage(file=iconPath))
    print.info(assetsPath)
    
    window.mainloop()