import cv2

#print(cv2.__version__)

#GÖRÜNTÜ OKUMA --> cv2.IMREAD  (oku numpy arraye kaydet,kendi çevirir)
#Her dosya türünü opencv okuyamaz.
#cv2.IMREAD_UNCHANGED(-1)  dokunma türüne
#cv2.IMREAD_GRAYSCALE(0) gri tonla okuma
#cv2.IMREAD_COLOR (1)    renkli okutma (default)
#BGR formatında okur renkli görüntüleri (blue,green,red)


I=cv2.imread('images/peppers.png',1)  #1 renkli oku, bgr formatında
print(type(I))
print(I.shape)
print(I.size)
print(I.dtype)  #uint8 görüntü için en iyi format
print(I.ndim)
print("*"*50)

#(1920,1080) (y,x) (sütun,satır)
#2D numpy dizinin ilk boyutu satırı temsil eder, her satır görüntünün yüksekliğini temsil eder

#görüntünün kopyasını alma ---> img.copy()

#ekranda gösterme ---> cv2.imshow('title',image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#cv2.imshow('peppers görüntü',I)
#cv2.waitKey(0) #tuşa bastıktan sonra 0 saniye bekle
#cv2.destroyAllWindows() #tüm pencereleri kapat
#print(I[50,50,:])  #50.satır 50.sütundaki yerleri göster  [71 39 66] [b,g,r]

#matploitlible görüntü gösterme  (rgb ye göre çalışır)

from matplotlib import pyplot as plt
plt.imshow(I)
plt.title('Image Peppers Orj')
plt.xticks([]) #eksenleri kaldırır
plt.yticks([]) #eksenleri kaldırır
#plt.imshow(I,cmap='Greys',interpolation='nearest')
#plt.imshow(I,cmap='binary',interpolation='nearest')
#plt.waitforbuttonpress()
#plt.close()

#opencv bgr okur,matplotlib rgb okur
print(I[250,50,:])
#I[50,53,:]=[0,0,0]  #0,0,0 siyah / 255,255,255 beyaz
#I[50:53,50:53,:]=np.ones((3,3,3))*255

#bgr'yi rgb yapma
I2=I.copy()
I2[:,:,0],I2[:,:,2]=I2[:,:,2],I2[:,:,0] #bgr rgb ---> 0 b idi sonra 2 b olsun !!!!!!!ÖNEMLİİİİ!!!!

Ir=I[:,:,2].copy()
Ig=I[:,:,1].copy()
Ib=I[:,:,0].copy()

I2[:,:,0]=Ir
I2[:,:,1]=Ig
I2[:,:,2]=Ib

#cv2.imshow('aa',I2)
#cv2.waitKey(0)

import numpy as np
I3=np.array([[255,193,105,55],[22,77,155,255],[255,0,255,0],[0,255,0,255]],dtype=np.uint8)
#cv2.imshow('aa',I3)
#cv2.waitKey(0)


#görünütünün boyutlarının ayırma-birleştirme  split-merge

I3=np.zeros((384,512,3),dtype=np.uint8)
IIb,IIg,IIr=cv2.split(I)

I3[:,:,0]=IIr
I3[:,:,1]=IIg
I3[:,:,2]=IIb

#cv2.imshow('aa',I3)
#cv2.waitKey(0)
#plt.imshow(I3)
#plt.waitforbuttonpress()
#plt.close()

#renk dönüşümleri
I4=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
I6=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
I5=cv2.imread('images/peppers.png',0)
cv2.imshow('a',I4)
cv2.imshow('ab',I5)
cv2.imshow('abc',I6)
cv2.waitKey(0)

I7=I.copy()
cv2.line(I7,(200,80),(450,80),(0,255,0),thickness=3)
cv2.imshow('I cizgi',I)
cv2.waitKey(0)

#








































