# coding=utf-8
# Filename: ch8_3.py\

def make_coffee(name="卡布奇诺"):
    return "制作一杯{0}咖啡。 ".format(name)

coffee1 = make_coffee("拿铁")
coffee2 = make_coffee()

print(coffee1)
print(coffee2)