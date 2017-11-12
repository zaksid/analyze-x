import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

IMG_LOGO = '../images/opencv_logo.jpg'
IMG_LOGO_NOISE = '../images/opencv_logo_noise.png'
IMG_EDGES = '../images/edges.png'

img = cv.imread(IMG_LOGO)

""" 2D Convolution (Image Filtering) """

kernel = np.ones((5, 5), np.float32) / 25
dst = cv.filter2D(img, -1, kernel)

""" Image Blurring (Image Smoothing)"""

# Averaging
blur = cv.blur(img, (5, 5))

# Gaussian Blurring
blur_g = cv.GaussianBlur(img, (5, 5), 0)

# Median Blurring
img_noise = cv.imread(IMG_LOGO_NOISE)
median = cv.medianBlur(img_noise, 5)

# Bilateral Filtering
# noise removal while keeping edges sharp
img_b = cv.imread(IMG_EDGES, )
smoothed = cv.bilateralFilter(img_b, 9, 75, 75)

# Display it

plt.subplot(341), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(342), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.subplot(343), plt.imshow(blur), plt.title('Blurred (Average)')
plt.xticks([]), plt.yticks([])

plt.subplot(344), plt.imshow(blur_g), plt.title('Gaussian Blurred')
plt.xticks([]), plt.yticks([])

plt.subplot(345), plt.imshow(img_noise), plt.title('Original (noise)')
plt.xticks([]), plt.yticks([])

plt.subplot(346), plt.imshow(median), plt.title('Median')
plt.xticks([]), plt.yticks([])

plt.subplot(349), plt.imshow(img_b), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(3, 4, 10), plt.imshow(smoothed), plt.title('Bilateral Filtering')
plt.xticks([]), plt.yticks([])

plt.show()
