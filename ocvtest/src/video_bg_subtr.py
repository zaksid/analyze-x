import cv2
import numpy as np

VIDEO_FILE = '../videos/video.mp4'
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
    '12':  np.array([[1056, 770], [975, 715], [1060, 690], [1160, 770]], np.int32),
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
    """
    :param img: Video frame to draw in
    :param pts: Points for polylines
    :param color: Color
    :return: None

    Draw filled semi transparent polygon on image
    """

    # Constant values
    opacity = 0.3
    thickness = 2

    # Draw boundaries of polygon
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, color, thickness)

    # Fill polygon
    overlay = img.copy()
    cv2.fillPoly(overlay, [pts], color)
    cv2.addWeighted(overlay, opacity, img, 1 - opacity, 0, img)

    return None


def draw_lanes(img, lanes, colors):
    """
    :param img: Video frame to draw in
    :param lanes: Dictionary with lane coordinates
    :param colors: Dictionary with colors
    :return: None

    Draw lane zones on video frame
    """

    for lane in lanes:
        draw_polygon(img, lanes[lane], colors[lane])

    return None


def qwerty():
    cap = cv2.VideoCapture(VIDEO_FILE)

    # take first frame of the video
    ret, frame = cap.read()

    fgbg = cv2.createBackgroundSubtractorMOG2()

    firstFrame = None

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

        draw_lanes(frame, LANES, COLORS)
        cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)

        cv2.imshow(WINDOW_NAME, frame)

        if cv2.waitKey(30) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


# def main():
qwerty()


# if __name__ == "__main__":
#     main
