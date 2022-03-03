import base64
from io import BytesIO
import cv2
from utils.area import AreaUtils
import os
import json


class Utils:
    """Calculate the Coordinate of BBox's Bottom Center Point

        Parameters
        ----------
        x1 : int
            bbox[0]
        y1 : int
            bbox[1]
        x2 : int
            bbox[2]
        y2 : int
            bbox[3]

        Returns
        -------
        (int, int)
            Returns the mean vector (8 dimensional) and covariance matrix (8x8
            dimensional) of the new track. Unobserved velocities are initialized
            to 0 mean.

        """
    @staticmethod
    def calculateBottomCenterCoordinate(x1, y1, x2, y2):
        x = (x1 + x2) / 2
        return [int(x), int(y2)]

    @staticmethod
    def isInside(toggle_x, toggle_y, new_x=0, new_y=0):
        PolygonShape = AreaUtils.getPolygonShape(
            json.loads(str(os.getenv('AREA'))))

        if not PolygonShape:
            return False

        nvert = len(PolygonShape)
        vertx = []
        verty = []
        testx = new_x
        testy = new_y
        for item in PolygonShape:
            vertx.append(item[0])
            verty.append(item[1])

        j = nvert - 1
        res = False
        for i in range(nvert):
            if (verty[j] - verty[i]) == 0:
                j = i
                continue
            x = (vertx[j] - vertx[i]) * (testy - verty[i]) / \
                (verty[j] - verty[i]) + vertx[i]
            if ((verty[i] > testy) != (verty[j] > testy)) and (testx < x):
                res = not res
            j = i

        return res

    @staticmethod
    def imageToBase64(image):
        retval, buffer = cv2.imencode('.jpg', image)
        jpgToText = base64.b64encode(buffer)
        return jpgToText
