import cv2
import numpy as np

I=cv2.imread('images/peppers.png',1)

M=np.array([[2,0,0],[0,0.5,0]],dtype=np.float32)

height,width=I.shape[0:2] #0 ve 1 i al

I2=cv2.warpAffine(I,M,(I.shape[1]*2,I.shape[0]//2))  # I2=cv2.warpAffine(I,M,(width*2,height//2))
#with-height  genişlik iki kat büyür,yükseklik yarıya düşer

print(I.shape)
print(I2.shape)

cv2.imshow('I',I)
cv2.imshow('I2',I2)


                                        #ÖTELEME (translation)

M2=np.array([[1,0,100],[0,1,50]],dtype=np.float32)    #100 br ssağa,50 br aşağıya kayacak
I3=cv2.warpAffine(I,M2,None)
cv2.imshow('I3',I3)

cv2.waitKey(0)
cv2.destroyAllWindows()

                                         #KONTRAST































