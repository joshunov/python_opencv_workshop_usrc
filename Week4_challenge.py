import cv2
import numpy as np

img = cv2.imread('..\Photos\Bughead.jpg')
cv2.imshow('Bughead', img)


cv2.waitKey(0)