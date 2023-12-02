import pyautogui as pag
import random
import time

# Coordinates of bazaar grid.  Change these with your coords using pag.displayMousePosition()
# six/four y are the Y values of the grid for the main bz interface, and sub menus, respectively
allX = {
    1: 1060,
    2: 1117,
    3: 1173,
    4: 1229,
    5: 1277,
    6: 1335,
    7: 1383,
    8: 1440,
    9: 1495,
}

sixY = {
    1: 447,
    2: 500,
    3: 557,
    4: 609,
    5: 665,
    6: 717,
}

fourY = {
    1: 504,
    2: 556,
    3: 611,
    4: 665,
}

def clickFour(x, y):
    clickAbsolute(allX[x], fourY[y])

def clickSix(x, y):
    clickAbsolute(allX[x], sixY[y])

# Clicks x, y with a random offset [to avoid detection]
def clickAbsolute(x, y):
    
    x = x + random.randint(-10, 10)
    y = y + random.randint(-10, 10)
    
    # Sleeps for random time to avoid detection
    toSleep = random.randint(200, 500) * 0.001
    time.sleep(toSleep)
    pag.moveTo(x, y)
    toSleep = random.randint(200, 500) * 0.001
    time.sleep(toSleep)
    pag.click()
    
#pag.displayMousePosition()
# Use above to map coords to your resolution