import cv2 as cv

VIDEO_FILE = '../videos/video.mp4'
VIDEO_SPEED = 15

cap = cv.VideoCapture(VIDEO_FILE)

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.namedWindow('camera1', cv.WINDOW_NORMAL)
    cv.imshow('camera1', gray)
    if cv.waitKey(VIDEO_SPEED) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
