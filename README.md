# JupiterAddons

Remaster of my prior MangoAddons

### How To Use
- Use pag.displayMousePosition() to grab coordinates for the following steps
- Map the dict in *mouseLib.py* with the coordinates of the bazaar grid for your resolution.  *sixY* and *fourY* are for the BZ main UI, and the sub-menus, respectively
- Install PyTesseract [https://pypi.org/project/pytesseract/]
- Change the text in Line 7 of *tess.py* to the path to your PyTess. executable
- Map the pixel range of your chat window to Line 21 of *tess.py*
- Ideally, download a smooth font texture pack[https://www.curseforge.com/minecraft/texture-packs/smooth-font/download/3765851]
- Face a dark block while macroing to avoid interferance [Obsidian or Black Wool work great]
- Start file *main.py* and switch to your minecraft window

### Mapping to a new item

*By default, the item is Volcanic Rock.  You can change this by altering functions in the main file*

- The functions *createBuyOrder()* and *createSellOrder()* are the only functions that need ot be altered
- Change the *clickSix()* function to navigate to your category, you will need two "six" functions if your item is not in the oddities category by default
- Change the click functions to navigate and buy order your item [A grid system is used, where the args are the X, Y values]
- Repeat the same for the sell function as well
