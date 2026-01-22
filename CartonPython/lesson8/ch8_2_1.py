# coding=utf-8
# Filename: ch8_2_1.py

def rect_area(width, height):
    area = width * height
    return area

r_area = rect_area(323, 646)
print("{0} x {1} 长方形的面积： {2:.2f}".format(323, 646, r_area))
