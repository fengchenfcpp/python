lst1 = "煮豆燃豆萁，豆在釜中泣。本是同根生，相见何太急？"
lst = list(lst1)
idx = lst.index("见")
lst[idx] = "煎"
print("".join(lst))