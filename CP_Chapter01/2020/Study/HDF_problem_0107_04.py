import cv2
import matplotlib.pyplot as plt
import numpy as np


def imgxor(rgb, bgr):
   simg = np.bitwise_xor(rgb, bgr)
   return simg


bgr = cv2.imread('ironman_1_des.jpg')
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

print(bgr.shape)
scode = np.random.randn(bgr.shape[0], bgr.shape[1], 3)
scode = np.abs(scode) * np.random.randint(150, 300)
scode = np.int32(scode)

simg = imgxor(rgb, scode)

print(simg[0, 0, :])
# plt.imshow(rgb)
plt.imshow(simg)

rgb2 = imgxor(simg, scode)

# plt.imshow(rgb2)