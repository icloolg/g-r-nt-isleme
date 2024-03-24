
import cv2
from matplotlib import pyplot as plt
I=cv2.imread('images/peppers.png',1)
I2 = cv2.imread('images/peppers.png')
px=I2[50,50]
px_blue=I2[50,50,0]
print(px)
print(px_blue)

I2[50,50]= [255,255,255]

cv2.imshow('Image Peppers with white dot',I2)
cv2.waitKey(0)
cv2.destroyAllWindows()



imageLine = I.copy()
pointA = (200,80)
pointB = (450,80)
cv2.line(imageLine, pointA, pointB, (255, 255, 0), thickness=3)
cv2.imshow('Image Line', imageLine)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Çember çizme:
#syntax : circle(image, center_coordinates, radius, color, thickness)
#Thickness = -1 yapılırsa daire çizer.

imageCircle = I.copy()
#circle_center = (415,190)
#radius =100
cv2.circle(imageCircle, (415,190), 100, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
cv2.imshow("Image Circle",imageCircle)
cv2.waitKey(0)
cv2.destroyAllWindows()


imageText = I.copy()
text = 'Merhaba Dunya'
#org = (50,350)
cv2.putText(imageText, text, (50,350), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1.5, color = (250,225,100))
cv2.imshow("Image Text",imageText)
cv2.waitKey(0)
cv2.destroyAllWindows()
