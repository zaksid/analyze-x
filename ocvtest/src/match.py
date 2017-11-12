import cv2 as cv
import numpy as np

IMG_IN = '../images/mario.jpg'
IMG_OUT = '../images/res_mario.png'

img_rgb = cv.imread(IMG_IN)
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
coin = img_gray[70:140, 84:98]
w, h = coin.shape[::-1]

res = cv.matchShapes(img_gray, coin, cv.TM_SQDIFF_NORMED, 0.0)
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255))

cv.imwrite(IMG_OUT, img_rgb)

out = cv.imread(IMG_OUT)
cv.imshow('coin', out)
cv.waitKey(0)
cv.destroyAllWindows()
