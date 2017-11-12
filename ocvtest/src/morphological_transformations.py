import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

IMG_J = '../images/j.png'
IMG_J_W = '../images/j_w.png'
IMG_J_B = '../images/j_b.png'
GRID_HEIGHT = 2
GRID_WIDTH = 6

img = cv.imread(IMG_J)
img_w = cv.imread(IMG_J_W)
img_b = cv.imread(IMG_J_B)

kernel = np.ones((5, 5), np.uint8)
kernel_9 = np.ones((9, 9), np.uint8)

""" Erosion """
# Erodes away the boundaries of foreground object (always try to keep foreground in white).
# A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1,
# otherwise it is eroded (made to zero).

# It is useful for removing small white noises, detach two connected objects etc.

erosion = cv.erode(img, kernel, iterations=1)

""" Dilation """
# Opposite of erosion.
# A pixel element is '1' if at least one pixel under the kernel is '1'.

# Increases the white region.
# In cases like noise removal, erosion is followed by dilation.
# Because, erosion removes white noises, but it also shrinks our object. So we dilate it.
# It is also useful in joining broken parts of an object.

dilation = cv.dilate(img, kernel, iterations=1)

""" Opening """
# Erosion followed by dilation

opening = cv.morphologyEx(img_w, cv.MORPH_OPEN, kernel)

""" Closing """
# Dilation followed by Erosion

closing = cv.morphologyEx(img_b, cv.MORPH_CLOSE, kernel)

""" Morphological Gradient """
# It is the difference between dilation and erosion of an image.
# The result will look like the outline of the object.

gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

""" Top Hat """
# The difference between input image and Opening of the image.

tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel_9)

""" Black Hat """
# The difference between the closing of the input image and input image.

blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel_9)

# Show everything on plot

plt.subplot(GRID_HEIGHT, GRID_WIDTH, 1), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(GRID_HEIGHT, GRID_WIDTH, 2), plt.imshow(erosion), plt.title('Eroded')
plt.xticks([]), plt.yticks([])

plt.subplot(GRID_HEIGHT, GRID_WIDTH, 3), plt.imshow(dilation), plt.title('Dilated')
plt.xticks([]), plt.yticks([])

plt.subplot(GRID_HEIGHT, GRID_WIDTH, 4), plt.imshow(gradient), plt.title('Gradient')
plt.xticks([]), plt.yticks([])

plt.subplot(GRID_HEIGHT, GRID_WIDTH, 5), plt.imshow(tophat), plt.title('Top Hat')
plt.xticks([]), plt.yticks([])

plt.subplot(GRID_HEIGHT, GRID_WIDTH, 6), plt.imshow(blackhat), plt.title('Black Hat')
plt.xticks([]), plt.yticks([])

plt.subplot(GRID_HEIGHT, GRID_WIDTH, 7), plt.imshow(img_w), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(GRID_HEIGHT, GRID_WIDTH, 8), plt.imshow(opening), plt.title('Opened')
plt.xticks([]), plt.yticks([])

plt.subplot(GRID_HEIGHT, GRID_WIDTH, 11), plt.imshow(img_b), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(GRID_HEIGHT, GRID_WIDTH, 12), plt.imshow(closing), plt.title('Closed')
plt.xticks([]), plt.yticks([])

plt.show()
