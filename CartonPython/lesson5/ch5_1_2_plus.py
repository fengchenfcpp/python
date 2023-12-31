# coding=utf-8
# Filename: ch5_1_2_plus.py

score = int(input("请输入一个0~100的整数："))

if score > 100:
    print("输入不正确，哪有这么多分啊！")
elif score == 100:
    print("哇哦，满分哦！你真棒！")
elif score >= 85:
    print("成绩不错！") 
elif score >= 60:
    print("加把劲！") 
elif score >= 0:
    print("不及格啦，这可不行！")     
else:
    print ("输入错误，没有负分！")    