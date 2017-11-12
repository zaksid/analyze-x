import cv2 as cv

IMG = '../images/cat.jpg'

img = cv.imread(IMG)
edges = cv.Canny(img, 100, 200, None, 3, False)

cv.imshow('Result', edges)
cv.waitKey(0)
cv.destroyAllWindows()
