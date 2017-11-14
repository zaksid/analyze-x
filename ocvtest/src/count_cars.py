import cv2
import numpy as np

VIDEO_FILE = '../videos/highway.mp4'
VIDEO_SPEED = 30

COLOR_AMBER = (255, 193, 7)
COLOR_AQUA = (117, 255, 234)
COLOR_BLUE = (255, 0, 0)
COLOR_CYAN = (128, 222, 234)
COLOR_GREEN = (0, 255, 0)
COLOR_INDIGO = (26, 35, 126)
COLOR_LIME = (205, 220, 57)
COLOR_MINT = (56, 247, 152)
COLOR_ORANGE = (255, 87, 34)
COLOR_PEACH = (255, 163, 84)
COLOR_PINK = (244, 143, 177)
COLOR_PURPLE = (126, 87, 194)
COLOR_TEAL = (77, 182, 172)
COLOR_RED = (0, 0, 255)
COLOR_VIOLET = (212, 52, 239)
COLOR_YELLOW = (0, 255, 255)

Lanes = {
    '1': {'x1': 260, 'y1': 412, 'x2': 433, 'y2': 412, 'color': COLOR_RED},
    '2': {'x1': 434, 'y1': 412, 'x2': 618, 'y2': 412, 'color': COLOR_BLUE},
    '3': {'x1': 619, 'y1': 412, 'x2': 800, 'y2': 412, 'color': COLOR_PINK},
    '4': {'x1': 801, 'y1': 412, 'x2': 985, 'y2': 412, 'color': COLOR_GREEN}
}

Counts = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0
}

gaussian_kernel = (5, 5)
kernel_3x3 = np.ones((3, 3), np.uint8)
kernel_5x5 = np.ones((5, 5), np.uint8)
thresh = 50

cap = cv2.VideoCapture(VIDEO_FILE)

fgbg = cv2.createBackgroundSubtractorMOG2()

while cap.isOpened():
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    blured = cv2.GaussianBlur(fgmask, gaussian_kernel, 0)
    closed = cv2.morphologyEx(blured, cv2.MORPH_CLOSE, kernel_3x3, iterations=3)
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel_3x3, iterations=3)
    ret, threshold = cv2.threshold(opened, thresh, 255, cv2.THRESH_BINARY)
    eroded = cv2.erode(threshold, kernel_5x5, iterations=3)
    dilated = cv2.dilate(eroded, kernel_5x5, iterations=3)

    result = dilated

    (_, contours, hierarchy) = cv2.findContours(result.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(frame, contours, -1, COLOR_AMBER, 2)
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Draw lanes
    for i in Lanes:
        x1 = Lanes[i]['x1']
        y1 = Lanes[i]['y1']
        x2 = Lanes[i]['x2']
        y2 = Lanes[i]['y2']
        color = Lanes[i]['color']

        cv2.line(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, 'COUNT %r: %r' % (i, Counts[i]), (x1, y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    for contour in contours:
        if cv2.contourArea(contour) < 250:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        center = x + w / 2
        cv2.rectangle(frame, (x, y), (x + w, y + h), COLOR_AMBER, 2)
        cv2.putText(frame, 'O', (center, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, COLOR_RED, 5)

        # Count vehicles on each lane
        for i in Lanes:
            x1 = Lanes[i]['x1']
            y1 = Lanes[i]['y1']
            x2 = Lanes[i]['x2']
            y2 = Lanes[i]['y2']
            color = Lanes[i]['color']

            if y1 < y < (y1 + 15) and x1 < center < x2:
                Counts[i] += 1

    # cv2.namedWindow('camera1', cv2.WINDOW_NORMAL)
    cv2.imshow('camera1', frame)
    # cv2.imshow('test', result)
    if cv2.waitKey(VIDEO_SPEED) & 0xFF == 27:
        break

print Counts
cap.release()
cv2.destroyAllWindows()
