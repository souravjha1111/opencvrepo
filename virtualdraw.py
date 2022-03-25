import cv2
import numpy as np
import time
import os
import handtrackingmodule as htm
brushthickness = 5
erasethickness = 8
overlayList = []
image = cv2.imread('/home/sourav/test/automation/collerpallet/2.png')
overlayList.append(image)
image = cv2.imread('/home/sourav/test/automation/collerpallet/1.png')
overlayList.append(image)
image = cv2.imread('/home/sourav/test/automation/collerpallet/0.png')
overlayList.append(image)
header = overlayList[0]
drawcolor =(255,0,0)
cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.65,maxHands=1)
canvas = np.zeros((480,650, 3), np.uint8)
xprev = 0
yprev = 0
while True:
    success, img = cap.read()
    print(cv2.getWindowImageRect('img'))
    img = cv2.flip(img, 1)
    img[10:54,16:60] = overlayList[1]
    img[10:54,100:144] = overlayList[0]
    img[10:54,200:244] = overlayList[2]
    img = detector.findHands(img, draw=True)
    lmlist = []
    fingers = []
    lmList= detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        x = lmList[8][1]
        y = lmList[8][2]
        x2 = lmList[12][1]
        y2 = lmList[12][2]
        fingers = detector.fingersUp()
        if fingers[1] and fingers[2]:
            xprev = 0
            yprev = 0
            if x2>=16 and x2<=60 and y2>=10 and y2<=54:
                drawcolor = (255,0,0)
            elif x2>=100 and x2<=144 and y2>=10 and y2<=54:
                drawcolor = (0,255,0)
            elif x2>=200 and x2<=244 and y2>=10 and y2<=54:
                drawcolor = (0,0,0)
            cv2.circle(img, (x2, y2), 15, drawcolor, cv2.FILLED)

        if fingers[1] and fingers[2] == False:
            if xprev == 0 and yprev == 0:
                xprev = x 
                yprev = y
            cv2.circle(img, (x, y), 15, drawcolor, cv2.FILLED)
            thickness =5
            if drawcolor == (0,0,0):
                thickness = erasethickness
            cv2.line(canvas, (xprev, yprev), (x, y), drawcolor, thickness)
            xprev = x
            yprev = y
    if all (x >= 1 for x in fingers):
        canvas = np.zeros((480,650, 3), np.uint8)
    canvas[10:54,16:60] = overlayList[1]
    canvas[10:54,100:144] = overlayList[0]
    canvas[10:54,200:244] = overlayList[2]


    imgGray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    # img = cv2.bitwise_and(img,imgInv)
    # img = cv2.bitwise_or(img,canvas)

    img = cv2.addWeighted(canvas, 0.5, img, 0.5, 0)
    cv2.imshow("Image", img)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(1)