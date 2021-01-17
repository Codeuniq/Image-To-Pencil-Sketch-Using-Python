import cv2

image_location = ""
filename = "rose1.jpg"

img = cv2.imread(image_location+filename)

gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted = 255 - gray_scale

Blurred = cv2.GaussianBlur(inverted,(21,21),0)

pencil = cv2.divide(gray_scale,inverted, scale=256.0 )

cv2.imshow("Orginal Image", img)
cv2.imshow("New Image", pencil)
cv2.waitKey(0)