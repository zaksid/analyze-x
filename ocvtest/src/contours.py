import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

IMG_CAT = '../images/cat.jpg'

# img = cv.imread(IMG_CAT)
# imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(imgray, 127, 255, 0)
# contours, hierarchy = cv.findContours(
#     thresh,  # src
#     cv.RETR_TREE,  # contour retrieval mode
#     cv.CHAIN_APPROX_SIMPLE  # contour approximation method
# )
#
# cv.imshow('Contours', contours)
# cv.waitKey(0)
# cv.destroyAllWindows()

IMG_STAR = '../images/star.png'

# img = cv.imread(IMG_STAR)
# img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # img = cv.invert(img)
# ret, thresh = cv.threshold(img, 127, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#
# cnt = contours[0]
# M = cv.moments(cnt)
#
# print M
#
# cv.imshow('Contours', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

img = cv.imread(IMG_CAT)
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hist = cv.calcHist(
    [imgray],   # source image of type uint8 or float32
    [0],        # channels. pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively
    None,       # mask image. To find histogram of full image, it is given as "None".
    [256],      # histSize (BIN count). For full scale, we pass [256].
    [0, 256]    # ranges. Normally, it is [0,256].
)

print hist

HEIGHT = 1
WIDTH = 2

plt.subplot(HEIGHT, WIDTH, 1), plt.imshow(imgray)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(HEIGHT, WIDTH, 2), plt.hist(imgray.ravel(), 256, [0, 256])
plt.title('Hist'), plt.xticks([0, 256]), plt.yticks([])

plt.show()
