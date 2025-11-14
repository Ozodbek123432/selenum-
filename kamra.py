import cv2
import time
import os
from datetime import datetime

# Papka yaratish
if not os.path.exists('rasmlar'):
    os.makedirs('rasmlar')

# Kamera ochish
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Kamera ochilmadi!")
    exit()

print("Kamera tayyor. 5 soniyadan keyin rasm olinadi...")
time.sleep(5)

# Rasm olish
ret, frame = camera.read()

if ret:
    # Vaqt bilan fayl nomi
    vaqt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fayl_nomi = f"rasmlar/rasm_{vaqt}.jpg"

    # Rasmni saqlash
    cv2.imwrite(fayl_nomi, frame)
    print(f"Rasm saqlandi: {fayl_nomi}")
else:
    print("Rasm olinmadi!")

# Kamera yopish
camera.release()