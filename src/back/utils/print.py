from termcolor import colored
from datetime import datetime

def success(m):
    t = "  SUCCESS  "
    c = "green"
    pta(t, c, m)
def error(m):
    t = "   ERROR   "
    c = "light_red"
    pta(t, c, m)
def fatal(m):
    t = "   FATAL   "
    c = "red"
    pta(t, c, m)
def info(m):
    t = "   INFO    "
    c = "blue"
    pta(t, c, m)
def warning(m):
    t = "  WARNING  "
    c = "yellow"
    pta(t, c, m)

def gt():
    m = datetime.now()
    fm = m.strftime("%H:%M:%S")
    return fm
def pta(t, c, m):
    fm = gt()
    print(
        colored(f"( {fm} )", "dark_grey", force_color=True)
        + " - " +
        colored(f"[{t}]", c, force_color=True)
        + " " + m
    )