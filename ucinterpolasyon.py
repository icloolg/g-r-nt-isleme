                                       #boyut değiştirme
                                      #_İNTERPOLASYON_


#cv2.INTER_NEAREST
#cv2.INTER_LINEAR
#cv2.INTER_CUBIC   >büyütmek için ideal
#cv2.INTER_AREA    >küçültmek için ideal



import cv2
import numpy as np

I=cv2.imread('images/peppers.png',1)
print(I.shape)
I2=cv2.resize(I,(800,400),interpolation=cv2.INTER_CUBIC)  #yeniden boyutlandırma (3840,2160)4k
I2=cv2.resize(I2,(512,384))
print(I2.shape)

I3=cv2.resize(I,None,fx=0.5,fy=1.5)  #Ölçek kullanarak boyutlandırma (width,height)
print(I3.shape)

I4=I[50:100,370:430]  #KIRPMA
I5=I[280:330,440:500]

print(I4.shape)
print(I5.shape)

#I[280:330,440:500]=I[50:100,370:430].copy()  #resme başka resim yapıştırma


aff = cv2.getRotationMatrix2D((I.shape[1]//2,I.shape[0]//2),angle=45,scale=1)
print(aff)
print(np.array([[np.cos(np.pi/4),np.sin(np.pi/4)],[-np.sin(np.pi/4),np.cos(np.pi/4)]]))

I6=cv2.warpAffine(I,aff,dsize=(None)) #dize=(512,384)

height,width=I.shape[:2]
inout_pts=np.float32([[0,0],[width-1,0],[0,height-1]])
output_pts=np.float32([[width-1,0],[0,0],[width-1,height-1]])
M=cv2.getAffineTransform(inout_pts,output_pts)
I7=cv2.warpAffine(I,M,None)  #ayna yansıması gibi
print(M)

cv2.imshow('orj',I)
cv2.imshow('I2',I2)
cv2.imshow('I3',I3)
cv2.imshow('kırpılmış',I4)
cv2.imshow('sarımsak',I5)
cv2.imshow('dondurme',I6)  #döndürme
cv2.imshow('I7',I7)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Temel Geometrik Görüntü İşleme Yöntemleri (geometric transformation)
#döndürme(rotation),ölçekleme(scaling),öteleme
#yeterlilikte afin dönüşüm hesaplama çıkabilir elle






