# from errno import ECHILD
# import imp
# import cv2
# import numpy as np
# import time
# import mediapipe as mp
# import math
# import handtrackingmodule as htm
# # from ctypes import cast, POINTER
# # from comtypes import CLSCTX_ALL
# # from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# ############################## VARIABLES ##############################
# ptime = 0
# wcam = 640
# hcam = 480

# #######################################################################

# cap = cv2.VideoCapture(0)
# cap.set(3, wcam)
# cap.set(4, hcam)


# detector = htm.handDetect(detectionCon = 0.7)


# # devices = AudioUtilities.GetSpeakers()
# # interface = devices.Activate(
# #     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# # volume = cast(interface, POINTER(IAudioEndpointVolume))
# # # volume.GetMute()
# # # volume.GetMasterVolumeLevel()
# # print(volume.GetVolumeRange())
# # # volume.SetMasterVolumeLevel(-20.0, None)

# lmlist = []
# while True:
#     success, img = cap.read()
#     img = detector.findhands(img = img, draw = True)
#     lmlist = detector.findposition(img, draw = False)
#     if len(lmlist) !=0:
#         x1, y1 = lmlist[4][1], lmlist[4][2]
#         x2, y2 = lmlist[8][1], lmlist[8][2]
#         cx , cy = (x2+x1)//2, (y2+y1)//2

#         cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)  
#         cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
#         cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
#         cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

#         length = math.hypot(x2-x1, y2-y1)
#         print(length)
#         if length<50:
#             cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

#     cTime = time.time()
#     frame = 1/(cTime - ptime)
#     ptime = cTime

#     cv2.putText(img, "FPS: " + str(int(frame)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#     cv2.imshow('img', img)
#     cv2.waitKey(1)





from errno import ECHILD
import imp
import cv2
import numpy as np
import time
import mediapipe as mp
import math
import handtrackingmodule as htm
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

############################## VARIABLES ##############################
ptime = 0
wcam = 640
hcam = 480

#######################################################################

cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)


detector = htm.handDetect(detectionCon = 0.7)


# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# # volume.GetMute()
# # volume.GetMasterVolumeLevel()
# print(volume.GetVolumeRange())
# # volume.SetMasterVolumeLevel(-20.0, None)

lmlist = []
while True:
    success, img = cap.read()
    img = detector.findhands(img = img, draw = True)
    lmlist = detector.findposition(img, draw = False)
    # if len(lmlist) !=0:
    #     x1, y1 = lmlist[4][1], lmlist[4][2]
    #     x2, y2 = lmlist[8][1], lmlist[8][2]
    #     cx , cy = (x2+x1)//2, (y2+y1)//2

    #     cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)  
    #     cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
    #     cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
    #     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

    #     length = math.hypot(x2-x1, y2-y1)
    #     print(length)
    #     if length<50:
    #         cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    cTime = time.time()
    frame = 1/(cTime - ptime)
    ptime = cTime

    cv2.putText(img, "FPS: " + str(int(frame)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('img', img)
    cv2.waitKey(1)


