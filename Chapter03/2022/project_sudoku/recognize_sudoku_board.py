from typing import List
import cv2
import numpy as np


# reference: https://youbidan.tistory.com/19


if __name__ == "__main__":
    folder_path = "Chapter03/2022/project_sudoku/"
    file_path = folder_path + 'sudoku_board_01.png'
    image_src = cv2.imread(file_path, cv2.IMREAD_COLOR)
    image_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    # cv2.imshow('image_gray', image_gray)
    # cv2.waitKey(0)

    blur = cv2.GaussianBlur(image_gray, ksize=(3,3), sigmaX=0)
    ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
    edged = cv2.Canny(blur, 10, 250)
    # cv2.imshow('Edged', edged)
    # cv2.waitKey(0)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow('Closed', closed)
    # cv2.waitKey(0)

    (cntrs, _) = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    total = 0
    
    cntrs_xy = np.array(cntrs)
    cntrs_xy.shape

    value: List = []
    for i in range(len(cntrs_xy)):
        for j in range(len(cntrs_xy[i])):
            value.append(cntrs_xy[i][j][0][0]) 
            x_min = min(value)
            x_max = max(value)
    
    y_min, y_max = 0,0
    value: List = []
    for i in range(len(cntrs_xy)):
        for j in range(len(cntrs_xy[i])):
            value.append(cntrs_xy[i][j][0][1])
            y_min = min(value)
            y_max = max(value)

    x = x_min
    y = y_min
    y_inc = int((y_max - y_min) / 9)
    x_inc = int((x_max - x_min) / 9)

    y_new = y
    for i in range(1, 10):
        y_cur = y_new
        y_new = y_cur + y_inc

        x_new = x
        for j in range(1, 10):
            x_cur = x_new
            x_new = x_cur + x_inc
            margin = 10
            img_trim = image_src[(y_cur + margin):(y_new - margin), 
                                 (x_cur + margin):(x_new - margin)]
            cv2.imshow('org_image', img_trim)
            cv2.waitKey(0)
    
    cv2.destroyAllWindows()
