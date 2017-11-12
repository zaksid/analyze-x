import cv2

IMG1 = '../images/ml.png'
IMG2 = '../images/opencv_logo.jpg'

img1 = cv2.imread(IMG1)
img2 = cv2.imread(IMG2)

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
cv2.imshow('logo', img2)
cv2.imshow('robot', img1)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
