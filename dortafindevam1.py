import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot

I=cv2.imread('images/cameraman.tif',-1)
print(I.shape)  #(256,256) siyah beyaz ya da gri tonlu bir resim

print("*"*50)

print('min:',np.min(I))
print('max:',np.max(I))
print('ort:',np.mean(I))

print("*"*50)

I2=np.int32(I)+50
I3=np.int32(I)-50

I2[I2>255]=255
I3[I3>255]=255
I2[I2>0]=0
I3[I3>0]=0

I2=np.uint8(I2)
I3=np.uint8(I3)


#I2=I+50
#I3=I-50

print('I2 min:',np.min(I2))   # I2 min: 0
print('I2 max:',np.max(I2))   # I2 max: 255
print('I2 ort:',np.mean(I2))  # I2 ort: 166.1854248046875
print("*"*50)

print('I3 min:',np.min(I3))    # I3 min: 0
print('I3 max:',np.max(I3))    # I3 max: 255
print('I3 ort:',np.mean(I3))   # I3 ort: 127.5330810546875

I4=255-I
I5=255-np.int16(I)
I5=np.int8(I5)

#uint8 işlemlerde sıkıntılı floata çevirmek daha sağlıklı


#I6=cv2.calcHist([I],[0],None,[256],(0,256))
#plt.plot(I6)
#plt.hist(I.ravel(),256,(0,256))
#plt.waitforbuttonpress()
#plt.close()

I7_orj=cv2.imread('images/peppers.png.',1)

colors=('b','g','r')
for i,renk in enumerate (colors):
    I7 = cv2.calcHist([I7_orj], [i], None, [256], (0, 256))
    plt.plot(I7,color=renk)

plt.waitforbuttonpress()
plt.close()


cv2.imshow('I',I)
#cv2.imshow('I2',I2)
#cv2.imshow('I3',I3)
#cv2.imshow('I4',I4)
#cv2.imshow('I6',I6)
cv2.imshow('I7',I7_orj)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Histogram Eşitleme    cv2.equalizeHist()
#bulunma olasılığı fazla olan piksellerin rengini aç,
# az olanların rengini kapat ki çok olanlar daha iyi ayırt edilebilsin