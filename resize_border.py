import cv2 


scenery = cv2.imread("assets/bilateral.jpg")
cv2.imshow("Scenery",scenery)

"""resized_scenery = cv2.resize(scenery,(850,250))
cv2.imshow("Resized Scenery",resized_scenery)"""

#adding border to the image
top,bottom,left,right = 10,10,10,10

#adding border style and properties
image_border = cv2.copyMakeBorder(scenery,top,bottom,left,right,borderType = cv2.BORDER_CONSTANT,value = [79,32,105] )#cv2.BORDER_REFLECT,cv2.BORDER_REPLICATE

#writing / saving a file
cv2.imwrite("assets/bordered_scenery.png",image_border)


cv2.imshow("Bordered Scenery",image_border)


cv2.waitKey(0)
cv2.destroyAllWindows()