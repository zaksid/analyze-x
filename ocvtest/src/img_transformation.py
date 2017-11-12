import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

IMG_CAT = '../images/cat.jpg'

# Resize
img_resize = cv.imread(IMG_CAT)

res1 = cv.resize(img_resize, None, fx=2, fy=3, interpolation=cv.INTER_CUBIC)

height, width = img_resize.shape[:2]
res2 = cv.resize(img_resize, (2 * width, 2 * height), interpolation=cv.INTER_CUBIC)

cv.imshow('orig', img_resize)
cv.imshow('res1', res1)
cv.imshow('res2', res2)

cv.waitKey(0)
cv.destroyAllWindows()

# Translate
img_translation = cv.imread(IMG_CAT, 0)
rows, cols = img_translation.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv.warpAffine(img_translation, M, (cols, rows))

cv.imshow('translation', dst)
cv.waitKey(0)
cv.destroyAllWindows()

# Rotation

img_rotate = cv.imread(IMG_CAT, 0)
rows, cols = img_rotate.shape

M = cv.getRotationMatrix2D(
    (cols / 2, rows / 2),  # center
    90,  # angle
    1  # scale
)

dest = cv.warpAffine(img_rotate, M, (cols, rows))

cv.imshow('Rotated', dest)
cv.waitKey(0)
cv.destroyAllWindows()

# Affine Transformation
img_affine = cv.imread(IMG_CAT)
rows, cols, ch = img_affine.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv.getAffineTransform(pts1, pts2)

dst = cv.warpAffine(img_affine, M, (cols, rows))

plt.subplot(121), plt.imshow(img_affine), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
