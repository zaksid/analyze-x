import cv2
import numpy as np

VIDEO_FILE = '../videos/video.mp4'
VIDEO_SPEED = 1
WINDOW_NAME = 'win'

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

kernel = np.ones((3, 3), np.uint8)

# lanes' coordinates
# top left, bottom left, bottom right, top right
LANES = {
    '1': np.array([[123, 0], [478, 286], [524, 273], [147, 0]], np.int32),
    '2': np.array([[148, 0], [525, 273], [563, 263], [180, 0]], np.int32),
    '3': np.array([[185, 0], [643, 302], [673, 293], [209, 0]], np.int32),
    '4': np.array([[210, 0], [673, 293], [708, 281], [240, 0]], np.int32),

    '5': np.array([[1185, 322], [1230, 348], [1370, 288], [1370, 256]], np.int32),
    '6': np.array([[1232, 350], [1266, 368], [1370, 321], [1370, 288]], np.int32),
    '7': np.array([[1266, 369], [1308, 392], [1370, 366], [1370, 321]], np.int32),
    '8': np.array([[1309, 392], [1358, 415], [1370, 410], [1370, 366]], np.int32),

    '9': np.array([[1330, 770], [1160, 640], [1210, 570], [1370, 755]], np.int32),
    '10': np.array([[1250, 770], [1115, 660], [1160, 640], [1330, 770]], np.int32),
    '11': np.array([[1160, 770], [1060, 690], [1115, 660], [1250, 770]], np.int32),
    '12': np.array([[1056, 770], [975, 715], [1060, 690], [1160, 770]], np.int32),

    '13': np.array([[340, 770], [352, 770], [453, 730], [477, 770]], np.int32),
    '14': np.array([[170, 770], [424, 685], [453, 731], [340, 770]], np.int32),
    '15': np.array([[170, 770], [0, 770], [393, 638], [424, 685]], np.int32),
    '16': np.array([[0, 770], [0, 715], [364, 598], [393, 638]], np.int32)
}

COLORS = {
    '1': COLOR_RED,
    '2': COLOR_GREEN,
    '3': COLOR_VIOLET,
    '4': COLOR_YELLOW,
    '5': COLOR_BLUE,
    '6': COLOR_MINT,
    '7': COLOR_PEACH,
    '8': COLOR_AQUA,
    '9': COLOR_INDIGO,
    '10': COLOR_PURPLE,
    '11': COLOR_CYAN,
    '12': COLOR_LIME,
    '13': COLOR_PINK,
    '14': COLOR_TEAL,
    '15': COLOR_ORANGE,
    '16': COLOR_AMBER
}


def draw_polygon(img, pts, color):
    """ Draw filled semi transparent polygon on image
    :param img: Video frame to draw in
    :param pts: Points for polylines
    :param color: Color
    :return: None
    """

    # Constant values
    # opacity = 0.2
    thickness = 2

    # Draw boundaries of polygon
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, color, thickness)

    # Fill polygon
    # overlay = img.copy()
    # cv2.fillPoly(overlay, [pts], color)
    # cv2.addWeighted(overlay, opacity, img, 1 - opacity, 0, img)

    return None


def draw_lanes(img, lanes, colors):
    """ Draw lane zones on video frame
    :param img: Video frame to draw in
    :param lanes: Dictionary with lane coordinates
    :param colors: Dictionary with colors
    :return: None
    """

    for lane in lanes:
        draw_polygon(img, lanes[lane], colors[lane])

    return None


def draw_contours(img, contours, contour_area, show_number=False):
    """ Draw contours according to their shapes
    :param img: Video frame to draw in
    :param contours: Contours to draw
    :param contour_area: Min area of contour. Smaller contours will be ignored
    :param show_number: Whether show contour number or not
    :return: Frame with rendered contours
    """

    for index, contour in enumerate(contours):
        if contour_area is not None and cv2.contourArea(contour) < contour_area:
            continue

        cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)

        if show_number:
            x, y, w, h = cv2.boundingRect(contour)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(
                img,
                str(index),  # text to write
                (x + w / 2, y + h / 2),  # bottom-left corner where data starts
                font,
                0.5,  # font scale
                (0, 0, 255),
                2  # thickness
            )

    return img


def draw_rectangle_contours(img, contours, contour_area):
    """ Draw rectangle contours
    :param img: Video frame to draw in
    :param contours: Contours to draw
    :param contour_area: Min area of contour. Smaller contours will be ignored
    :return: Frame with rendered contours
    """
    for contour in contours:
        if contour_area is not None and cv2.contourArea(contour) < contour_area:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        # print "x: {0:3d}, y: {0:3d}, w: {0:3d}, h: {0:3d}".format(x, y)
        cv2.rectangle(img, (x, y), (x + w, y + h), (200, 255, 170), 2)

    return img


def draw_rotated_rectangle_contours(img, contours, contour_area):
    """ Draw rotated rectangle contours
    :param img: Video frame to draw in
    :param contours: Contours to draw
    :param contour_area: Min area of contour. Smaller contours will be ignored
    :return: Frame with rendered contours
    """
    for contour in contours:
        if contour_area is not None and cv2.contourArea(contour) < contour_area:
            continue

        rect = cv2.minAreaRect(contour)

        box = cv2.boxPoints(rect)
        box = np.int0(box)
        img = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

    return img


def process_frame(fgmask, frame):
    # Constants
    contour_area = 130
    thresh = 50
    gaussian_kernel = (7, 7)
    kernel_3x3 = np.ones((3, 3), np.uint8)
    kernel_5x5 = np.ones((5, 5), np.uint8)
    ###########

    # True original color frame
    frame_color = frame

    # Processed frame
    # frame_gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
    frame_gray = fgmask
    frame_gray = cv2.GaussianBlur(frame_gray, gaussian_kernel, 0)

    frame_gray = cv2.morphologyEx(frame_gray, cv2.MORPH_CLOSE, kernel_5x5, iterations=3)
    frame_gray = cv2.morphologyEx(frame_gray, cv2.MORPH_OPEN, kernel_5x5, iterations=3)

    ret, threshold = cv2.threshold(frame_gray, thresh, 255, cv2.THRESH_BINARY)
    # threshold = cv2.adaptiveThreshold(frame_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # ret, threshold = cv2.threshold(threshold, thresh, 255, cv2.THRESH_BINARY)
    threshold = cv2.erode(threshold, kernel_5x5, iterations=3)

    (_, contours, hierarchy) = cv2.findContours(threshold.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours as a rectangle
    # frame_color = draw_rectangle_contours(frame_color, contours, contour_area)

    frame_color = draw_rotated_rectangle_contours(frame_color, contours, contour_area)

    # Draw contours
    # frame_color = draw_contours(frame_color, contours, contour_area, True)

    return frame_color


def qwerty():
    cap = cv2.VideoCapture(VIDEO_FILE)

    # take first frame of the video
    ret, frame = cap.read()

    fgbg = cv2.createBackgroundSubtractorMOG2()

    # firstFrame = None

    while True:
        ret, frame = cap.read()
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame = cv2.GaussianBlur(frame, (7, 7), 0)

        # if firstFrame is None:
        #     firstFrame = frame
        #     continue
        #
        # frameDelta = cv2.absdiff(firstFrame, frame)
        # thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

        # thresh = cv2.dilate(thresh, None, iterations=1)
        # (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        fgmask = fgbg.apply(frame)

        # fgmask = cv2.erode(fgmask, kernel, iterations=1)
        # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

        fgmask = cv2.threshold(fgmask, 15, 255, cv2.THRESH_BINARY)[1]

        frame = process_frame(fgmask, frame)

        # draw_lanes(frame, LANES, COLORS)

        # Draw lanes' contours
        for cnt in LANES:
            cv2.drawContours(frame, [LANES[cnt]], -1, (0, 255, 255), 2)

        cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)

        cv2.imshow(WINDOW_NAME, frame)

        if cv2.waitKey(VIDEO_SPEED) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


# def main():
qwerty()


# if __name__ == "__main__":
#     main
