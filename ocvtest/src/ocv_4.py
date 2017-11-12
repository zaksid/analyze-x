import cv2 as cv

IMG_CAT = '../images/cat.jpg'

# Load an color image in grayscale
img = cv.imread(IMG_CAT, 0)
# cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)
key = cv.waitKey(0) & 0xFF

if key == 27:
    cv.destroyAllWindows()
