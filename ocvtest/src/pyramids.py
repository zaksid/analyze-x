import cv2 as cv
import numpy as np, sys

IMG_CAT = '../images/cat.jpg'
IMG_APPLE = '../images/apple.png'
IMG_ORANGE = '../images/orange.png'

img = cv.imread(IMG_CAT)
apple = cv.imread(IMG_APPLE)
orange = cv.imread(IMG_ORANGE)

lower_res = cv.pyrDown(img)

cv.imshow('lower_res', lower_res)
cv.waitKey(0)
cv.destroyAllWindows()

higher_res = cv.pyrUp(lower_res)
cv.imshow('higher_res', higher_res)
cv.waitKey(0)
cv.destroyAllWindows()

# generate Gaussian pyramid for apple
G = apple.copy()
gpA = [G]
for i in xrange(6):
    G = cv.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for orange
G = orange.copy()
gpO = [G]
for i in xrange(6):
    G = cv.pyrDown(G)
    gpO.append(G)

# generate Laplacian Pyramid for apple
lpA = [gpA[5]]
for i in xrange(5, 0, -1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i - 1], GE)
    lpA.append(L)

# generate Laplacian Pyramid for orange
lpO = [gpO[5]]
for i in xrange(5, 0, -1):
    GE = cv.pyrUp(gpO[i])
    L = cv.subtract(gpO[i - 1], GE)
    lpO.append(L)

# Now add left and right halves of images in each level
LS = []
for la, lo in zip(lpA, lpO):
    rows, cols, dpt = la.shape
    ls = np.hstack(
        (la[:, 0:cols / 2],
         lo[:, cols / 2:])
    )
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in xrange(1, 6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack(
    (apple[:, :cols / 2],
     orange[:, cols / 2:])
)

cv.imwrite('Pyramid_blending2.jpg', ls_)
cv.imwrite('Direct_blending.jpg', real)
