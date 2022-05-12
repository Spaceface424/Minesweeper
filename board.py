import pyautogui as pgui
import numpy as np
import screenshot

#board is (682, 392, 540, 480)
#cells are 30x30


numRows = 14
numCols = 18
arr = np.zeros((numRows, numCols))
def screenshotArray():
    for row in range(14):
        for col in range(18):
            if pgui.pixelMatchesColor(697 + (30 * col), 407 + (30 * row), (229, 194, 159), tolerance=3): #blank spaces
                arr[row][col] = 9
            if pgui.pixelMatchesColor(697 + (30 * col), 407 + (30 * row), (215, 184, 153), tolerance=3): #blank spaces
                arr[row][col] = 9
            if pgui.pixelMatchesColor(697 + (30 * col), 407 + (30 * row), (25, 118, 210), tolerance=3):
                arr[row][col] = 1
            if pgui.pixelMatchesColor(697 + (30 * col), 407 + (30 * row), (62, 144, 64), tolerance=20):
                arr[row][col] = 2
            if pgui.pixelMatchesColor(697 + (30 * col), 407 + (30 * row), (213, 62, 58), tolerance=10):
                arr[row][col] = 3
            if pgui.pixelMatchesColor(701 + (30 * col), 409 + (30 * row), (123, 31, 162), tolerance=40):
                arr[row][col] = 4
            if pgui.pixelMatchesColor(697 + (30 * col), 404 + (30 * row), (255, 143, 0), tolerance=20):
                arr[row][col] = 5
            if pgui.pixelMatchesColor(697 + (30 * col), 404 + (30 * row), (242, 54, 8), tolerance=10): #flags
                arr[row][col] = 8
            # #0's are covered spaces
    print(arr)

def play():
    for rows in range(14):
        for cols in range(18):
            # need to add edge cases if condition
            if 1 <= arr[rows][cols] <= 5:
                if rows != 0 and cols != 0 and rows != 13 and cols != 17:
                    nonEdgeClicks(rows, cols)
                # else:
                #     edgeClicks(rows, cols)

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
    if flagCounter == arr[rows][cols]:
        screenshot.middleClick(rows, cols)
    elif blankCounter == arr[rows][cols] or (blankCounter + flagCounter == arr[rows][cols] and blankCounter != 0):
        for z in range(int((len(spaces))/2)):
            screenshot.rightClick(spaces.item(2*z), spaces.item(2*z+1))
            arr[np.int16(spaces[2*z]).item()][np.int16(spaces[2*z+1]).item()] = 8
            print(rows, cols)
            print(spaces.item(2*z), spaces.item(2*z+1))
    print(arr)
#
# def edgeClicks(rows, cols):
#     bruh
def test():
    screenshotArray()
    play()

test()
