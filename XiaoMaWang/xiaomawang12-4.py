a = "欢迎来到小码王"
lst = list(a)
for i in range(len(a)):
    lst[i] += str(i+1)
print("".join(lst))