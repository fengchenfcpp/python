poem = "江南好，风景旧曾。日出江花红胜火，春来江水绿如蓝。能不忆江南啊？"
poemList = list(poem)
poemList.insert(8, "谙")
poemList.remove("啊")

for i in poemList:
    print(i, end="")
    if i == "。":
        print()