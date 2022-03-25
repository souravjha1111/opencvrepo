import cv2
import handtrackingmodule as htm
cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.75)
fingerspointspositionid = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    fingersfoundarray = []
    if len(lmList) != 0:
        fingersfoundarray = []
        if lmList[fingerspointspositionid[0]][1] > lmList[fingerspointspositionid[0] - 1][1]:
            fingersfoundarray.append(1)
        else:
            fingersfoundarray.append(0)
        for id in range(1, 5):
            if lmList[fingerspointspositionid[id]][2] < lmList[fingerspointspositionid[id] - 2][2]:
                fingersfoundarray.append(1)
            else:
                fingersfoundarray.append(0)

        totalFingers = fingersfoundarray.count(1)
        cv2.putText(img, str(totalFingers), (0, 100), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 10)

    cv2.imshow("Image", img)
    cv2.waitKey(1)