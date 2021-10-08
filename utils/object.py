import base64
from io import BytesIO
import cv2
from utils.utils import Utils

class ObjectUtils:
    @staticmethod
    def writeCircleStatusOnFrame(frame, toggle_x, toggle_y, x, y):
        if Utils.isInside(toggle_x, toggle_y, x, y) == True:
            cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)
        elif Utils.isInside(toggle_x, toggle_y, x, y) == False:
            cv2.circle(frame, (x, y), 5, (255, 255, 255), -1)


