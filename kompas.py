import numpy as np
import cv2
from cv2 import aruco
from enum import Enum


class Side(Enum):
    NORTH = 0
    SOUTH = 1

frame = cv2.imread('images/blenderCompas.png')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters =  aruco.DetectorParameters_create()
dict = aruco.custom_dictionary_from(1,4,aruco_dict)

corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, dict, parameters=parameters)

if ids is not None:
    print(Side.NORTH)
else:
    print(Side.SOUTH)


frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
cv2.imshow('image',frame_markers)
cv2.waitKey(0)
cv2.destroyAllWindows()





