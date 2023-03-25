
def erase_line():
    print("\33[K", end = "")

def gotoXY(x, y):
    print("\33[%d;%dH" % (x, y), end = "")

def gotoUp(y):
    print("\33[1F", end = "")
    print("\33[%dG" % (y), end = "")