import cv2
import numpy as np

#I=cv2.imread('images/fig1.jpg',-1)
I=cv2.imread('images/circles.png.',0)
print(I.shape)

#se=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(35,35))
se=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(17,17))
#se2=np.array[[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0]] #kendimiz çubuk gibi bir matris oluşturduk (filtre)



I2=cv2.erode(I,se) #ı2 erojın yapılmış resim
I3=cv2.dilate(I,se)
I4=cv2.morphologyEx(I,cv2.MORPH_OPEN,se)   #orijinal görüntüme "opening"yap,kernel(se) yapılandırma ögesi
I5=cv2.morphologyEx(I,cv2.MORPH_CLOSE,se)  #orijinal görüntüme "closing"yap
I5_test1=cv2.morphologyEx(I,cv2.MORPH_DILATE,se) #closing testi önce dilate sonra o görüntüye erode
I5_test2=cv2.morphologyEx(I5_test1,cv2.MORPH_ERODE,se)
#I5=cv2.morphologyEx(I,cv2.MORPH_CLOSE,se2)


print(np.sum(np.sum(I5-I5_test2))) #closing ile denediğimiz test arasındaki fark 0 =aynı şeyi yaparlar
print(se.shape)
#print(se2.shape)
#print(se2.dtype)
#print(se2)
print(se.dtype)
print(se) #elips bir görüntü verir

cv2.imshow('kernel',se*255) #elips görüntü
cv2.imshow('Orj',I)
cv2.imshow('dilated',I3)
cv2.imshow('opening',I4)
cv2.imshow('closing',I5)
cv2.imshow('closing2',I5_test2)
#cv2.imshow('eroded',I)

cv2.waitKey(0)
cv2.destroyAllWindows()