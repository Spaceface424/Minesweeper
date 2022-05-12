import pyautogui as pygui

startx = 682
starty = 392
dimension = 30
# def screenshot():
#     pygui.screenshot("board.png", region=(startx, starty, 540, 480))

def getXCoordinate(column):
    return column*dimension+startx+15

def getYCoordinate(row):
    return row*dimension+starty+15

# def cellScreenshot(filename, row, column):
#     pygui.screenshot(filename, region=(getYCoordinate(row), getXCoordinate(column), dimension, dimension))

def rightClick(row, column):
    pygui.rightClick(x=getXCoordinate(column), y=getYCoordinate(row))

def middleClick(row,column):
    pygui.middleClick(x=getXCoordinate(column), y=getYCoordinate(row))