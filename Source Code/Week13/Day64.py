import cv2

### Bài 1
image = cv2.imread('data/input.jpg')

cv2.imshow('Window Name', image)

### Bài 2
cv2.imwrite('output.jpg', image)

### Bài 3
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('Window Name', image_rgb)

### Bài 4
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('Window Name', image_hsv)

### Bài 5
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Window Name', image_gray)
cv2.imwrite('gray.jpg', image_gray)

### Bài 6
combined = cv2.hconcat([image_rgb, image_hsv])
cv2.imshow('Window Name', combined)

cv2.waitKey(0) 
cv2.destroyAllWindows() 