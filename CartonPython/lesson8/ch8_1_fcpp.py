# coding=utf-8
# Filename: ch8_1_fcpp.py

def rect_area(length, width):
    """计算矩形面积"""
    area = length * width
    return area

def rect_perimeter(length, width):
    """计算矩形周长"""
    perimeter = 2 * (length + width)
    return perimeter

def print_rect_info(length, width):
    """打印矩形信息"""
    area = rect_area(length, width)
    perimeter = rect_perimeter(length, width)
    print(f"Length: {length}, Width: {width}, Area: {area}, Perimeter: {perimeter}")