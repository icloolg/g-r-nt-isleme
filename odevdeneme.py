import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('images/frozen_rose.jpg')

# Görüntünün boyutlarını al
height, width, _ = image.shape

# Parçaları oluşturmak için boyutları hesapla
piece_width = width // 3  # Genişliği 3 eşit parçaya böleceğiz
piece_height = height // 2  # Yüksekliği 2 eşit parçaya böleceğiz

# Her bir parçanın boyutu
piece_size = (piece_height + 10, piece_width + 10, 3)  # Çizgi eklenmiş boyut

# Parçaları saklamak için liste oluştur
pieces = []

# Parçaları oluştur ve her birine çizgiler ekleyin
for i in range(2):  # Yükseklik boyunca döngü
    for j in range(3):  # Genişlik boyunca döngü
        # Köşe koordinatları
        top_left_x = j * piece_width
        top_left_y = i * piece_height
        bottom_right_x = (j + 1) * piece_width
        bottom_right_y = (i + 1) * piece_height
        # Görüntüyü kes
        piece = image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
        # Kenarlara beyaz çizgiler ekleyin
        piece[:, :5] = [255, 255, 255]  # Sol kenar
        piece[:, -5:] = [255, 255, 255]  # Sağ kenar
        piece[:5, :] = [255, 255, 255]  # Üst kenar
        piece[-5:, :] = [255, 255, 255]  # Alt kenar
        # Parçayı listeye ekle
        pieces.append(piece)

# Parçaları birleştir
merged_image = np.vstack([np.hstack(pieces[:3]), np.hstack(pieces[3:])])

# Görüntüyü göster
cv2.imshow("Merged Image", merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
