import base64
from io import BytesIO
import cv2

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
    def isInside(toggle_x, toggle_y, new_x = 0, new_y = 0):
        if (toggle_y < new_y):
            return True
        else:
            return False 
        # x = (-new_y + 3074.83 ) / 2.31
        # if new_x > x:
        #     return True
        # else:
        #     return False
    
    @staticmethod
    def imageToBase64(image):
        retval, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer)
        return jpg_as_text