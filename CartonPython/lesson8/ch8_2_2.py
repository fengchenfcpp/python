# coding=utf-8
# Filename: ch8_2_2.py

def rect_area(width, height):
    area = width * height
    return area

r_area = rect_area(width=335, height=467)
print("{0} x {1} 长方形的面积：{2:2f}".format(335, 467, r_area))

r_area = rect_area(height=467, width=335)
print("{0} x {1} 长方形的面积：{2:2f}".format(467, 335,  r_area))
