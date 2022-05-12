import pyautogui as pgui
import numpy as np
import screenshot
import time
#board is (682, 392, 540, 480)
#cells are 30x30

numRows = 14
numCols = 18
arr = np.zeros((numRows, numCols))
def screenshotArray():
	  startXCoord = boardLoc()[0]
  startYCoord = boardLoc()[1]
  
    for row in range(14):
        for col in range(18):
            if pgui.pixelMatchesColor((697+ (30 * col), s407+ (30 * row), (229, 194, 159), tolerance=3): #blank spaces
                arr[row][col] = 9
            if pgui.pixelMatchesColor(s697+ (30 * col), s407+ (30 * row), (215, 184, 153), tolerance=3): #blank spaces
                arr[row][col] = 9
            if pgui.pixelMatchesColor(s697+ (30 * col), s407+ (30 * row), (25, 118, 210), tolerance=3):
                arr[row][col] = 1
            if pgui.pixelMatchesColor(s697+ (30 * col), s407+ (30 * row), (62, 144, 64), tolerance=20):
                arr[row][col] = 2
            if pgui.pixelMatchesColor(s697+ (30 * col), s407+ (30 * row), (213, 62, 58), tolerance=10):
                arr[row][col] = 3
            if pgui.pixelMatchesColor(s701  (30 * col), s409+ (30 * row), (123, 31, 162), tolerance=40):
                arr[row][col] = 4
            if pgui.pixelMatchesColor(s697+ (30 * col), s404+ (30 * row), (255, 143, 0), tolerance=20):
                arr[row][col] = 5
            if pgui.pixelMatchesColor(s697+ (30 * col), s404+ (30 * row), (242, 54, 8), tolerance=10): #flags
                arr[row][col] = 8
            # #0's are covered spaces
    print(arr)

def play():
      for rows in range(14):

        for cols in range(18):

            if 1 <= arr[rows][cols] <= 5:

                if rows != 0 and cols != 0 and rows != 13 and cols != 17:

                    nonEdgeClicks(rows, cols)

                else:

                    edgeClicks(rows, cols)
def nonEdgeClicks(rows, cols):
    blankCounter = 0
    flagCounter = 0
    spaces = np.array([])

    for x in range(-1, 2):
        for y in range(-1, 2):
            if arr[x + rows][y + cols] == 0:
                blankCounter += 1
                spaces = np.append(spaces, np.array([x + rows, y + cols]))
            elif arr[x + rows][y + cols] == 8:
                flagCounter += 1

    click(blankCounter, flagCounter, spaces, rows, cols)

def edgeClicks(rows, cols):
    blankCounter = 0

    flagCounter = 0

    spaces = np.array([])

    if rows == 0:
      
      for x in range(-1, 2):

        for y in range(0, 2):

            if arr[x + rows][y + cols] == 0:

                blankCounter += 1

                spaces = np.append(spaces, np.array([x + rows, y + cols]))

            elif arr[x + rows][y + cols] == 8:

                flagCounter += 1

    if rows == 13:

      for x in range(-1, 2):

        for y in range(-1, 1):

            if arr[x + rows][y + cols] == 0:

                blankCounter += 1

                spaces = np.append(spaces, np.array([x + rows, y + cols]))

            elif arr[x + rows][y + cols] == 8:

                flagCounter += 1

    if cols == 0:

      for x in range(0, 2):

        for y in range(-1, 2):

            if arr[x + rows][y + cols] == 0:

                blankCounter += 1

                spaces = np.append(spaces, np.array([x + rows, y + cols]))

            elif arr[x + rows][y + cols] == 8:

                flagCounter += 1

    if cols == 17:

      for x in range(-1, 1):

        for y in range(-1, 2):

            if arr[x + rows][y + cols] == 0:

                blankCounter += 1

                spaces = np.append(spaces, np.array([x + rows, y + cols]))

            elif arr[x + rows][y + cols] == 8:

                flagCounter += 1
              
    click(blankCounter, flagCounter, spaces, rows, cols)

def click(blankCounter, flagCounter, spaces, rows, cols):
  
  if flagCounter == arr[rows][cols]:

        screenshot.middleClick(rows, cols)

    elif blankCounter + flagCounter == arr[rows][cols]:

        for z in range(int((len(spaces))/2)):

            screenshot.rightClick(spaces.item(2*z), spaces.item(2*z+1))

            arr[np.int16(spaces[2*z]).item()][np.int16(spaces[2*z+1]).item()] = 8
          

def test():
  time.sleep(2)
  screenshotArray()
  play()


test()
