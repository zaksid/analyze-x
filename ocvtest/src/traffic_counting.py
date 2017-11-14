import cv2

backsub = cv2.createBackgroundSubtractorMOG2()  # background subtraction to isolate moving cars
capture = cv2.VideoCapture('../videos/video.mp4')
i = 0
minArea = 1
while True:
    ret, frame = capture.read()
    fgmask = backsub.apply(frame, None, 0.01)
    erode = cv2.erode(fgmask, None, iterations=3)  # erosion to erase unwanted small contours
    moments = cv2.moments(erode, True)  # moments method applied
    area = moments['m00']

    # x1, y1, x2, y2 = 478, 286, 563, 263

    x1, y1, x2, y2 = 200, 286, 1563, 263

    cv2.line(
        frame,  # image where you want to draw the shapes
        (x1, y1),  # start point
        (x2, y2),  # end point
        (0, 0, 255),
        2
    )

    if moments['m00'] >= minArea:
        x = int(moments['m10'] / moments['m00'])
        y = int(moments['m01'] / moments['m00'])
        if x > x1 and x < x2 and y > y1 and y < y2:  # range of line coordinates for values on left lane
            i = i + 1
            print(i)
        elif x > 102 and x < 110 and y > 105 and y < 130:  # range of line coordinatess for values on right lane
            i = i + 1
            print(i)
        print(x,y)
        cv2.putText(frame, 'COUNT: %r' % i, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2)
        cv2.imshow("Track", frame)
        # cv2.imshow("background sub", fgmask)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
