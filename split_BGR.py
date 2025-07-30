import cv2

open_cv = cv2.imread("assets/opencv.png")
cv2.imshow("Original",open_cv)

#spliting the image in bgr saturations
blue_saturation,green_saturation,red_saturatuon = cv2.split(open_cv)

cv2.imshow("Blue saturation",blue_saturation)
cv2.imshow("Green saturation",green_saturation)
cv2.imshow("Red saturatuion",red_saturatuon)

cv2.waitKey(0)
cv2.destroyAllWindows()