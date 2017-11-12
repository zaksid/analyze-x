import cv2 as cv
from matplotlib import pyplot as plt

IMG_GRADIENT_BW = '../images/gradient_bw.png'
IMG_SUDOKU = '../images/sudoku.png'
IMG_NOISY = '../images/noisy.png'

"""" Simple Thresholding """

# If pixel value is greater than a threshold value, it is assigned one value (may be white),
# else it is assigned another value (may be black).

img = cv.imread(IMG_GRADIENT_BW)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh1 = cv.threshold(
    img,  # grayscale image
    127,  # threshold value which is used to classify the pixel values
    255,  # value to be given if pixel value is more than (sometimes less than) the threshold value
    cv.THRESH_BINARY  # style of thresholding
)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

""" Adaptive Thresholding """

# The algorithm calculates the threshold for a small regions of the image. So we get different thresholds
# for different regions of the same image and it gives us better results for images with varying illumination.

img_a = cv.imread(IMG_SUDOKU, 0)
img_a = cv.medianBlur(img_a, 5)

ret, th1 = cv.threshold(img_a, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(
    img_a,  # src
    255,    # max value
    cv.ADAPTIVE_THRESH_MEAN_C,  # Adaptive Method - decides how thresholding value is calculated.
    cv.THRESH_BINARY,           # thresholdType
    11,     # Block Size - decides the size of neighbourhood area
    2       # C - a constant which is subtracted from the mean or weighted mean calculated.
)
th3 = cv.adaptiveThreshold(img_a, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

titles = [
    'Original Image',
    'Global Thresholding (v = 127)',
    'Adaptive Mean Thresholding',
    'Adaptive Gaussian Thresholding'
]
images = [img_a, th1, th2, th3]

for i in xrange(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

""" Otsu's Binarization """

# It automatically calculates a threshold value from image histogram for a bimodal image.
# (bimodal image is an image whose histogram has two peaks)
img_o = cv.imread(IMG_NOISY, 0)

# global thresholding
ret1, th1 = cv.threshold(img_o, 127, 255, cv.THRESH_BINARY)

# Otsu's thresholding
ret2, th2 = cv.threshold(img_o, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv.GaussianBlur(img_o, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# plot all the images and their histograms
images = [img_o, 0, th1,
          img_o, 0, th2,
          blur,  0, th3]

titles = ['Original Noisy Image',    'Histogram', 'Global Thresholding (v=127)',
          'Original Noisy Image',    'Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

for i in xrange(3):
    plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])

plt.show()

