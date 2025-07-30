import cv2

grey_ghost_image = cv2.imread("assets/ghost.png",0)#Zero is for grayscaled image and 1 is for colored image and by defult color code is 1
cv2.imshow("Ghost",grey_ghost_image)

cv2.waitKey(0)
cv2.destroyAllWindows()