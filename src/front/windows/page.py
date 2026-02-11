import webview as wv
import os
import src.back.utils.print as print

class Api:
    def printSomething(self):
        print.debug("hello")

def startUp(whereTo):
    def loadCSS(window):
        whereCss = os.path.join(os.path.dirname(__file__), "style.css")
        with open(whereCss, "r") as f:
            css = f.read()
        window.load_css(css)
        
    currentPath = os.path.dirname(__file__)
    indexPath = os.path.join(currentPath, whereTo, "index.html")
    
    window = wv.create_window(
        'WhatsAnApp - Settings',
        indexPath,
        js_api=Api(),
        
        width=400,
        height=600
    )
    
    window.events.loaded += loadCSS
    wv.start(
        private_mode=False,
        http_server=True
    )
