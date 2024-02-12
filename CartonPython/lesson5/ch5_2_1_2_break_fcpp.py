# coding=utf-8
# Filename: ch5_2_1_2_break_fcpp.py

i = 0

while i * i < 901:
    i += 1
    if i == 29:
        break
    print(str(i) + '*' + str(i) + ' =', i * i)
else:
    print('While over!') 