# coding=utf-8
# Filename: ch5_4_for_fcpp.py

i = 100; r = 0; s = 0; t = 0

while i < 5000000:
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i == (r ** 3 + s ** 3 + t ** 3):
        print("i = " + str(i))

    i += 1 