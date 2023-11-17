lst=["张飞", "关羽", "刘备", "诸葛亮", "赵子龙", "曹操"]
count = 0
for i in lst:
    print(i+(10-len(i))*" ", end="")
    count += 1
    if count % 2 == 0:
        print()