# Exercise 1.7 - 4
# title   : Encryption of image
# version : 2022.02.20.

from secrets import token_bytes
from typing import Tuple, Any

import cv2
import numpy
import sys


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")


# encode() only available for str
def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_keys: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_keys ^ dummy
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


# Encryption of color image
# size 25 > 51 
def color_image_encrypt(ori_source: numpy.ndarray) -> Tuple[numpy.ndarray, numpy.ndarray]:
    row, col, depth = ori_source.shape  # image information
    arr_encrypted = numpy.zeros((row, col, depth))
    arr_dummy = numpy.zeros((row, col, depth))

    for i in range(row):
        for j in range(col):
            for k in range(depth):
                # print(sys.getsizeof(ori_source[i][j][k]))
                # print(sys.getsizeof(str(ori_source[i][j][k])))
                arr_encrypted[i][j][k], arr_dummy[i][j][k] = encrypt(str(ori_source[i][j][k]))
    return arr_dummy, arr_encrypted
# end of color_image_encrypt


# Decryption of color image
def color_image_decrypt(key1: numpy.ndarray, key2: numpy.ndarray) -> numpy.ndarray:
    row, col, depth = key1.shape  # image information
    arr_decrypted = numpy.zeros((row, col, depth))

    for i in range(row):
        for j in range(col):
            for k in range(depth):
                arr_decrypted[i][j][k] = decrypt(int(key1[i][j][k]), int(key2[i][j][k]))

    return arr_decrypted
# end of color_image_decrypt


# 인터넷에서 가져온 이미지의 경우 encrypt - decrypt 과정에서 용량 증가
# 이 코드로 만든 이미지는 encrypt - decrypt 과정에서 용량 변화 X
if __name__ == "__main__":
    folder_path = "CP_Chapter01/2022/Exercise/"
    img = cv2.imread(folder_path + "Bob_src.jpeg", cv2.IMREAD_COLOR)

    test_dummy, test_encrypted = color_image_encrypt(img)
    test_decrypted = color_image_decrypt(test_dummy, test_encrypted)

    cv2.imwrite(folder_path + "Bob_des.jpeg", test_decrypted)
