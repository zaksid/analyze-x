import cv2
import numpy as np

GAUSSIAN_KERNEL = (5, 5)
KERNEL_3x3 = np.ones((3, 3), np.uint8)
KERNEL_5x5 = np.ones((5, 5), np.uint8)
THRESH_GRAY = 127
THRESH_VAL = 30


def process_frame(frame):
    """
    Apply image processing algorithms to video frame.
    :param frame: Video frame to process
    :return: Processed video frame
    """
    blured = cv2.GaussianBlur(frame, GAUSSIAN_KERNEL, 0)
    closed = cv2.morphologyEx(blured, cv2.MORPH_CLOSE, KERNEL_3x3, iterations=5)
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, KERNEL_3x3, iterations=1)
    ret, threshold_0 = cv2.threshold(opened, THRESH_GRAY, 255, cv2.THRESH_TOZERO)
    ret, threshold = cv2.threshold(threshold_0, THRESH_VAL, 255, cv2.THRESH_BINARY)
    # eroded = cv2.erode(threshold, KERNEL_5x5, iterations=3)
    dilated = cv2.dilate(threshold, KERNEL_5x5, iterations=5)

    result = dilated

    return result
