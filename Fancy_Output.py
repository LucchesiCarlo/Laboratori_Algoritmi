
from enum import IntEnum

#https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters
#Riferimenti per la codicia ANSI

class graphic(IntEnum):
    Normal = 0
    Bold = 1
    Italic = 3
    Underline = 4 


class color(IntEnum):
    Black = 30
    Red = 31
    Green = 32
    Yellow = 33
    Blue = 34
    BrightRed = 91


def erase_line():
    print("\33[K", end = "")

def gotoXY(x, y):
    print("\33[%d;%dH" % (x, y), end = "")

def gotoUp(y):
    print("\33[1F", end = "")
    print("\33[%dG" % (y), end = "")

def format_text(color, graphic = graphic.Normal):
    print("\33[%dm" % (graphic), end = "")
    print("\33[%dm" % (color), end = "")

def print_formatted(text, color, graphic = graphic.Normal, end = "\n"):
    print("\33[%dm" % (graphic), "\33[%dm" % (color), text, "\33[m", end = end, sep = "")

def reset_format():
    print("\33[m", end = "")