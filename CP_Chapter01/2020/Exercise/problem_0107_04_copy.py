# title   : Encryption of image
# version : 1.0 (2020.08.03)
# author  : kobong
# email   : cleverkobong@gmail.com
from secrets import token_bytes
from typing import Tuple

import cv2
import numpy


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")


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


def color_image_encrypt(ori_source: numpy.ndarray) -> Tuple[int, int, int, int, int]:
    row, col, depth = ori_source.shape  # image information
    vec_source = img.reshape(row * col * depth, 1, order='c')  # reshape image to 1d numpy.ndarray
    print(type(vec_source))
    byt_source = vec_source.tobytes()
    print(byt_source)
    print(type(byt_source))
    str_source = str(byt_source)  # bytes to string
    print(str_source)
    print(type(str_source))
    dummy, encrypted = encrypt(str_source)
    return dummy, encrypted, row, col, depth


def color_image_decrypt(key1: int, key2: int, row: int, col: int, depth: int) -> numpy.ndarray:
    str_result = decrypt(key1, key2)
    print(str_result)
    print(type(str_result))
    byt_result = str_result.encode()
    byt_result = byt_result[2:-1]
    print(byt_result)
    print(type(byt_result))


if __name__ == "__main__":
    img = cv2.imread("python.png", cv2.IMREAD_COLOR)
    # print(img)
    e_key1, e_key2, v_row, v_col, v_depth = color_image_encrypt(img)
    color_image_decrypt(e_key1, e_key2, v_row, v_col, v_depth)

    # e_key1, e_key2 = encrypt("One Time Pad!")

    # cv2.imwrite('test.png', test)
    # cv2.imshow('Original', test)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
