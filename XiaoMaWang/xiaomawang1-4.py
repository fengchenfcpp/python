#!/usr/bin/python
# Filename: xiaomawang1-4.py
yuwen = 85
shuxue = 95
yingyu = 90
kexue = 98
tiyu = 92

max_val = max(yuwen, shuxue, yingyu, kexue, tiyu)
min_val = min(yuwen, shuxue, yingyu, kexue, tiyu)
average_val = (yuwen+shuxue+yingyu+kexue+tiyu)/5

print('最高分：', max_val,'分')
print('最低分：', min_val,'分')
print('平均分：', average_val,'分')