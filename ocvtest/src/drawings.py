import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

""" Line """
# Draw a diagonal blue line with thickness of 5 px
cv.line(
    img,          # image where you want to draw the shapes
    (0, 0),       # start point
    (511, 511),   # end point
    (255, 0, 0),  # color  - as a tuple for RGB. For grayscale, just pass the scalar value
    5             # thickness of the line (default is 1). If -1 is passed for closed figures, it will fill the shape.
)

""" Rectangle """
# Draw a green rectangle with thickness of 3 px
cv.rectangle(
    img,
    (384, 0),    # top-left corner
    (510, 128),  # bottom-right corner
    (0, 255, 0),
    3
)

""" Circle """
# Draw a red filled circle
cv.circle(
    img,
    (447, 63),  # center
    63,         # radius
    (0, 0, 255),
    -1
)

""" Ellipse """
# Draw ellipse
cv.ellipse(
    img,
    (256, 256),  # center
    (100, 50),   # axis length
    0,    # angle of rotation of ellipse in anti-clockwise direction
    0,    # starting of ellipse arc measured in clockwise direction from major axis
    180,  # ending of ellipse arc measured in clockwise direction from major axis
    255,  # color
    -1    # filled
)

""" Polygon """
# Draw a polygon
# coordinates of vertices
pts = np.array([
    [10, 5],
    [20, 30],
    [70, 20],
    [50, 10]
], np.int32)
pts = pts.reshape((-1, 1, 2))

# cv2.polylines() can be used to draw multiple lines.
# Just create a list of all the lines you want to draw and pass it to the function.
# All lines will be drawn individually. It is a much better and faster way to draw a group of lines
# than calling cv2.line() for each line.
cv.polylines(
    img,
    [pts],
    True,  # isClosed. If argument is False, you will get a polylines joining all the points, not a closed shape
    (0, 255, 255)
)

""" Text """
# Add text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(
    img,
    'OpenCV',   # text to write
    (10, 500),  # position coordinates of where to put text (i.e. bottom-left corner where data starts)
    font,
    4,          # font scale
    (255, 255, 255),
    2,          # thickness
    cv.LINE_AA  # line type
)

cv.imshow('Drawings', img)
key = cv.waitKey(0)

cv.destroyAllWindows()
