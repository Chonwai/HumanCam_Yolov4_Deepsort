import base64
from io import BytesIO


class AreaUtils:
    """Get the Polygon Shape

        Parameters
        ----------
        polygonVertices : object
            {"x1": 402,"y1": 234,"x2": 497,"y2": 182,.....}

        Returns
        -------
        (int, int)
            Returns the mean vector (8 dimensional) and covariance matrix (8x8
            dimensional) of the new track. Unobserved velocities are initialized
            to 0 mean.

    """
    @staticmethod
    def getPolygonShape(polygonVertices):
        areaPolygon = []

        verticeslength = len(polygonVertices)
        if verticeslength % 2 is not 0:  # Polygon coordinates must be multiples of 2
            return []
        verticesIndexMax = verticeslength // 2

        # "x1": 402,"y1": 234,"x2": 497,"y2": 182,.....
        for i in range(0, verticesIndexMax):
            index = str(i + 1)
            x_index = 'x' + index
            y_index = 'y' + index
            one_poly = [polygonVertices[x_index],
                        polygonVertices[y_index]]
            areaPolygon.append(one_poly)

        return areaPolygon
