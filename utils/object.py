import base64
from io import BytesIO
import cv2
from utils.utils import Utils

class ObjectUtils:
    @staticmethod
    def writeCircleStatusOnFrame(frame, width, height, x, y):
        if Utils.isInside(width, height, x, y) == True:
            cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)
        elif Utils.isInside(width, height, x, y) == False:
            cv2.circle(frame, (x, y), 5, (255, 255, 255), -1)


