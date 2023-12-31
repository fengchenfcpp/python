# coding=utf-8
# Filename: ch5_1_3.py

score = int(input("请输入一个0~100的整数："))
grade = "N"

if score > 100:
    print("输入不正确，哪有这么多分啊！")
elif score == 100:
    grade = "A+"
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 0:
    grade = "F"
else:
    print ("输入错误，没有负分！")      

print("Grade = " + grade)

