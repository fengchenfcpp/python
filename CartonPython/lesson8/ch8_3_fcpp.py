# coding=utf-8
# Filename: ch8_3_fcpp.py

def make_coffee(coffee_type="普通", sugar=0, milk=0):
    """制作咖啡"""
    print(f"制作一杯{coffee_type}咖啡，糖量: {sugar}，牛奶量: {milk}")

coffee1 = make_coffee("拿铁", sugar=2, milk=1)
coffee2 = make_coffee("美式", sugar=1)
coffee3 = make_coffee()

print (coffee1)
print (coffee2)
print (coffee3)