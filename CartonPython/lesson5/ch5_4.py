# coding=utf-8
# Filename: ch5_3_2.py

i = 198; r = 0; s = 0; t = 0

while i < 1000:
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i == (r ** 3 + s ** 3 + t ** 3):
        print("i = " + str(i))

    i += 1 