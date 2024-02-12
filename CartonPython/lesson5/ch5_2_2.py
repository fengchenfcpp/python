# coding=utf-8
# Filename: ch5_2_2.py

i = 0

while i * i < 100000000:
    i += 1
    print(str(i) + '*' + str(i) + ' =', i * i)
else:
    print('While Over')