import mouseLib as ml
import pyautogui as pag
import time
import random
import tess

# Basic functions
def noSus(toType):
    for char in toType:
        pag.press(char)
        delay = random.randint(5, 10) * 0.001
        print("[DELAY] " + str(delay))
        time.sleep(delay)
        
def get_pixel_color(x, y):
    color = pag.pixel(x, y)
    return color

def checkGUI():
    if get_pixel_color(1031, 525) == (198, 198, 198):
        pag.press("escape")
    
def checkChat():
    if get_pixel_color(18, 1373) == (224, 224, 224):
        print("[INFO] ChatTest Passed")
    else:
        print("[ERROR] ChatTest Failed")
        pag.press("/")

# Bazaar utilities
def createBuyOrder():
    print("[FUNCTION] createBuyOrder()")
    print("[INFO] Creating buy order...")
    noSus("bz")
    pag.press("enter")
    ml.clickSix(3, 4)
    ml.clickFour(3, 2)
    ml.clickFour(7, 2)
    ml.clickFour(7, 2)
    ml.clickFour(8, 2)
    time.sleep(0.2)
    pag.press("1")
    time.sleep(0.2)
    ml.clickAbsolute(1278, 749)
    ml.clickFour(4, 2)
    ml.clickFour(5, 2)
    time.sleep(0.5)
    pag.press("/")
    

def cancelBuyOrder():
    print("[FUNCTION] cancelBuyOrder()")
    print("[INFO] Canceling buy order...")
    noSus("bz")
    pag.press("enter")
    ml.clickSix(6, 6)
    time.sleep(0.2)
    ml.clickFour(2, 3)
    time.sleep(0.2)
    ml.clickFour(3, 2)
    time.sleep(0.2)
    pag.press("escape")
    time.sleep(2)
    pag.press("/")
    

def claimBuyOrder():
    print("[FUNCTION] claimBuyOrder()")
    print("[INFO] Claiming buy order...")
    noSus("bz")
    pag.press("enter")
    ml.clickSix(6, 6)
    ml.clickFour(2, 3)
    pag.press("escape")
    time.sleep(2)
    pag.press("/")
    
    
def createSellOrder():
    print("[FUNCTION] createSellOrder()")
    print("[INFO] Creating sell order...")
    noSus("bz")
    pag.press("enter")
    ml.clickSix(3, 4)
    ml.clickFour(3, 2)
    ml.clickFour(7, 2)
    ml.clickFour(8, 2)
    ml.clickFour(4, 2)
    ml.clickFour(5, 2)
    time.sleep(2)
    pag.press("/")
    
    
def cancelSellOrder():
    print("[FUNCTION] cancelSellOrder()")
    print("[INFO] Canceling sell order...")
    noSus("bz")
    pag.press("enter")
    ml.clickSix(6, 6)
    time.sleep(0.2)
    ml.clickFour(2, 2)
    time.sleep(0.2)
    ml.clickFour(5, 2)
    time.sleep(0.2)
    pag.press("escape")
    time.sleep(2)
    pag.press("/")
    

def claimSellOrder():
    print("[FUNCTION] claimSellOrder()")
    print("[INFO] Claiming sell order...")
    noSus("bz")
    pag.press("enter")
    ml.clickSix(6, 6)
    ml.clickFour(2, 2)
    pag.press("escape")
    time.sleep(2)
    pag.press("/")

# Cycles [Main funcs 1/2]
def cycle1():
    pag.press("/")
    createBuyOrder()
    while True:
        if "OUTDATED" in tess.main() or "MATCHED" in tess.main():
            cancelBuyOrder()
            checkGUI()
            time.sleep(1)
            checkChat()
            createBuyOrder()
        elif "filled" in tess.main() and "Buy" in tess.main():
            claimBuyOrder()
            time.sleep(2)
            checkGUI()
            time.sleep(5)
            checkChat()
            createSellOrder()
            cycle2()
            
def cycle2():
    while True:
        if "OUTDATED" in tess.main() or "MATCHED" in tess.main():
            cancelSellOrder()
            time.sleep(1)
            checkChat()
            createSellOrder()
        elif "filled" in tess.main() and "Sell" in tess.main():
            claimSellOrder()
            time.sleep(2)
            checkGUI()
            time.sleep(1)
            cycle1()

# Starts program on a 3sec delay [to switch to mc window]
time.sleep(3)
cycle1()