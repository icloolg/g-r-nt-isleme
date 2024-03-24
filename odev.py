

import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('images/frozen_rose.jpg')

# Görüntünün boyutlarını al
height, width, _ = image.shape

# Parçaları oluşturmak için boyutları hesapla
piece_width = width // 3  # Genişliği 3 eşit parçaya böleceğiz
piece_height = height // 2  # Yüksekliği 2 eşit parçaya böleceğiz

# Parçaları saklamak için liste oluştur
pieces = []

# Parçaları oluştur
for i in range(2):  # Yükseklik boyunca döngü
    for j in range(3):  # Genişlik boyunca döngü
        # Köşe koordinatları
        top_left_x = j * piece_width
        top_left_y = i * piece_height
        bottom_right_x = (j + 1) * piece_width
        bottom_right_y = (i + 1) * piece_height
        # Görüntüyü kes ve parçayı listeye ekle
        piece = image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
        pieces.append(piece)

# Her parçanın altına ve üstüne siyah çizgiler ekleyin
for i in range(3):
    pieces[i] = np.vstack([pieces[i], np.zeros((5, piece_width, 3), dtype=np.uint8)])  # Altına çizgi ekle
    pieces[i] = np.vstack([np.zeros((5, piece_width, 3), dtype=np.uint8), pieces[i]])  # Üstüne çizgi ekle

# Her parçanın arasına siyah bir çizgi ekleyin
for i in range(1, len(pieces)):
    pieces[i][:, :5] = 0  # Sol kenarı siyahla doldur

# Parçaları birleştir
merged_image = np.vstack([np.hstack(pieces[:3]), np.hstack(pieces[3:])])

print(image.shape)
# Birleştirilmiş görüntüyü göster
cv2.imshow("Merged Image with Lines", merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
