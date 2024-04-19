# coding=utf-8
# Filename: ch5_2_1_2_snow.py

i = 0

while i * i < 100099:
    i += 1
    if i == 55:
        break
    print(str(i) + '*' + str(i) + ' =', i * i)
else:
    print('While Over')