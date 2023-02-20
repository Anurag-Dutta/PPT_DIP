import cv2
import numpy as np


def function(parameters):
    ...

    ...
    return cv2.LUT(parameters)


img = cv2.imread('moon_original.jpg')
modified_img = function(...)

cv2.imshow('Original image', img)
cv2.imshow('Modified image', modified_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
