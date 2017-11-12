import numpy as np
import cv2 as cv

WINDOW_NAME = 'image'


def nothing(x):
    pass


img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow(WINDOW_NAME)

# create trackbars for color change
cv.createTrackbar('R', WINDOW_NAME, 0, 255, nothing)
cv.createTrackbar('G', WINDOW_NAME, 0, 255, nothing)
cv.createTrackbar('B', WINDOW_NAME, 0, 255, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, WINDOW_NAME, 0, 1, nothing)
while 1:
    cv.imshow(WINDOW_NAME, img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

    # get current positions of four trackbars
    r = cv.getTrackbarPos('R', WINDOW_NAME)
    g = cv.getTrackbarPos('G', WINDOW_NAME)
    b = cv.getTrackbarPos('B', WINDOW_NAME)
    s = cv.getTrackbarPos(switch, WINDOW_NAME)

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()
