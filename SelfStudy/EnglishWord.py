import random
print("欢迎来到千词斩")


qList=["随机","继续","硬币","答案"]
aList=["random","continue","coin","answer"]

f=random.randint(0,3)
co=0
while True:
    f=random.randint(0,3)
    a=qList[f]
    if a==None:
        continue
    b=aList[f]
    c=input("请问"+a+"的英文单词是:")
    if c==b:
        co=co+1
        if co==10:
            print("你背下了所有单词")
            break
        qList[f]=None
        print("√")
    else:
        print("×")
