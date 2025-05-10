import cv2
import numpy as np

# Load image
img_original = cv2.imread('data/2.jpg')
img_original = cv2.resize(img_original, (640, 480))

# Apply Gaussian Filter with kernel matrix 5x5 , sigma = 1
img_filtered = cv2.GaussianBlur(img_original, (5, 5), 1)
# cv2.imshow('Window Name', img_filtered)


def gaussian_kernel(size, sigma):
    if size % 2 == 0:
        size = size + 1

    max_point = size // 2 # both directions (x,y) maximum cell start point
    min_point = - max_point # both directions (x,y) minimum cell start point

    K = np.zeros((size, size)) # kernel matrix
    for x in range(min_point, max_point + 1):
        for y in range(min_point, max_point + 1):
            value = (1 / (2 * np.pi * sigma**2)) * np.exp(-(x**2 + y**2) / (2 * sigma**2))
            K[x - min_point, y - min_point] = value

    return K

kernel = gaussian_kernel(5, 1.4)

img_gaussian = cv2.filter2D(img_original, -1, kernel)
combined = cv2.hconcat([img_filtered, img_gaussian])
cv2.imshow('Window Name', combined)
cv2.waitKey(0) 
cv2.destroyAllWindows() 