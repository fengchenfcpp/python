# coding=utf-8
# Filename: ch5_1_2.py

score = int(input("请输入一个0~100的整数："))

if score >= 60:
    if score >= 85:
        print("你真优秀！")
    else:
        print("你的成绩还可以！")
else:
    print("你需要加倍努力！") 