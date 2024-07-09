

import cv2

img1 = cv2.imread("F:\\shihab_pic_1.jpg")
img1 = cv2.resize(img1, (700,700))
print("Image printed")
print(img1)
print("Image printed")
cv2.imshow("original",img1)

#printing gray scale image

img2 = cv2.imread("F:\\shihab_pic_1.jpg",0)
img2 = cv2.resize(img2, (700,700))
print("Image printed")
print("Image printed")
cv2.imshow("Gary image",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

