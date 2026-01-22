# coding=utf-8
# Filename: ch8_2_1_fcpp.py

def rect_area(length, width):
    """计算矩形面积"""
    area = length * width
    return area
r_area=rect_area(5, 3)
print(f"矩形面积为: {r_area}")

def rect_perimeter(length, width):
    """计算矩形周长"""
    perimeter = 2 * (length + width)
    return perimeter
r_perimeter=rect_perimeter(5, 3)
print(f"矩形周长为: {r_perimeter}")

def print_rect_info(length, width):
    """打印矩形信息"""
    area = rect_area(length, width)
    perimeter = rect_perimeter(length, width)
    print(f"Length: {length}, Width: {width}, Area: {area}, Perimeter: {perimeter}")
print_rect_info(5, 3)