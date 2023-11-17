a = []
i = 1
while True:
    if i % 3 == 0:
        if i % 5 == 0:
            a.append(i)
    if i == 100:
        break
    i += 1
print(a)