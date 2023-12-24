# coding=utf-8
# Filename: ch5_1_1.py

score = int(input("请输入一个0~100整数："))

if score >= 85:
    print("你真优秀")

if score < 60:
    print("你需要加倍努力！")
    
if (score >= 60) and (score < 85):
    print("你的成绩还不错！")