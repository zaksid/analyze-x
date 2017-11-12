import cv2
import numpy as np

""" Constants """
IMG = '../images/test_frame.png'
# IMG = '../images/Selection_001.png'
# IMG = '../images/test_frame.png'
CONTOUR_AREA = 130
THRESH = 50
GAUSSIAN_KERNEL = (7, 7)
kernel_3x3 = np.ones((3, 3), np.uint8)
kernel_5x5 = np.ones((5, 5), np.uint8)

"""""" """"""


def process_frame(frame):
    # True original color frame
    frame_color = frame

    # Processed frame
    frame_gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.GaussianBlur(frame_gray, GAUSSIAN_KERNEL, 0)

    frame_gray = cv2.morphologyEx(frame_gray, cv2.MORPH_CLOSE, kernel_5x5, iterations=3)
    frame_gray = cv2.morphologyEx(frame_gray, cv2.MORPH_OPEN, kernel_5x5, iterations=3)

    ret, threshold = cv2.threshold(frame_gray, THRESH, 255, cv2.THRESH_BINARY)
    # threshold = cv2.adaptiveThreshold(frame_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # ret, threshold = cv2.threshold(threshold, THRESH, 255, cv2.THRESH_BINARY)
    threshold = cv2.erode(threshold, kernel_5x5, iterations=3)

    (_, contours, hierarchy) = cv2.findContours(threshold.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours as a rectangle
    for contour in contours:
        # contour = component[0]
        # hierarchyC = component[1]
        if cv2.contourArea(contour) < CONTOUR_AREA:
            continue

        # if hierarchyC[3] < 0:
        #     continue

        (x, y, w, h) = cv2.boundingRect(contour)
        # print "x: {0:3d}, y: {0:3d}, w: {0:3d}, h: {0:3d}".format(x, y)
        cv2.rectangle(frame_color, (x, y), (x + w, y + h), (200, 255, 170), 2)

    # Draw contours
    for index, contour in enumerate(contours):
        if cv2.contourArea(contour) < CONTOUR_AREA:
            continue

        cv2.drawContours(frame_color, [contour], -1, (0, 255, 0), 2)

        (x, y, w, h) = cv2.boundingRect(contour)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(
            frame_color,
            str(index),  # text to write
            (x + w / 2, y + h / 2),
            # position coordinates of where to put text (i.e. bottom-left corner where data starts)
            font,
            0.5,  # font scale
            (0, 0, 255),
            2  # thickness
        )

    frame_processed = threshold

    cv2.imshow('test', frame_color)
    # cv2.imshow('test', frame_processed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    frame = cv2.imread(IMG)
    process_frame(frame)


if __name__ == "__main__":
    main()
