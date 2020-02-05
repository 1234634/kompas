import numpy as np
import cv2
from cv2 import aruco
from enum import Enum


class Side(Enum):
    NORTH = 0
    SOUTH = 1

    
frame = cv2.imread('images/markers2.png')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters =  aruco.DetectorParameters_create()

corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)

'''
if(corners[1] > 0):
    print(Side.NORTH)
else:
    print(Side.SOUTH)
'''



cv2.imshow('image',frame_markers)
cv2.waitKey(0)
cv2.destroyAllWindows()




