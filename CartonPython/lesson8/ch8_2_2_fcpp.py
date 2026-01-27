# coding=utf-8
# Filename: ch8_2_2_fcpp.py

def rect_area(length, width):
    """计算矩形面积"""
    area = length * width
    return area

r_area = rect_area(length=7123.123, width=4456.456)
print("{0} * {1}矩形面积为: {2:.2f}".format(7123.123, 4456.456, r_area))