import cv2 as cv
from matplotlib import pyplot as plt

IMG = '../images/sudoku.png'
IMG_CAT = '../images/cat.jpg'

img = cv.imread(IMG, 0)

laplacian = cv.Laplacian(img, cv.CV_64F)
sobel_x = cv.Sobel(img, cv.CV_64F, dx=1, dy=0, ksize=5)
sobel_y = cv.Sobel(img, cv.CV_64F, dx=0, dy=1, ksize=5)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 3), plt.imshow(sobel_x, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4), plt.imshow(sobel_y, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

img = cv.imread(IMG_CAT)
laplacian_cat = cv.Laplacian(img, cv.CV_64F)

cv.imshow('Laplacian Cat', laplacian_cat)
cv.waitKey(0)
cv.destroyAllWindows()
