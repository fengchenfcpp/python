a = ["12", "23", 35, "45", 89]
b = [11, 34, 75, "54", "78"]
c = [0, 0, 0, 0, 0]
c[0] = int(a[0]) + b[0]
c[1] = int(a[1]) + b[1]
c[2] = str(a[2]) + str(b[2])  # b[2] = str(a[2]+b[2])
c[3] = str(int(a[3])+int(b[3]))
c[4] = b[4] + str(a[4])
print(c)


