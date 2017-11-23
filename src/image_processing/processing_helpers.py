import cv2
import numpy as np

GAUSSIAN_KERNEL = (5, 5)
KERNEL_3x3 = np.ones((3, 3), np.uint8)
KERNEL_5x5 = np.ones((5, 5), np.uint8)
thresh = 50


def process_frame(frame):
    blured = cv2.GaussianBlur(frame, GAUSSIAN_KERNEL, 0)
    closed = cv2.morphologyEx(blured, cv2.MORPH_CLOSE, KERNEL_3x3, iterations=5)
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, KERNEL_3x3, iterations=1)
    ret, threshold = cv2.threshold(opened, thresh, 255, cv2.THRESH_BINARY)
    # eroded = cv2.erode(threshold, KERNEL_5x5, iterations=3)
    dilated = cv2.dilate(threshold, KERNEL_5x5, iterations=5)

    result = threshold

    return result
