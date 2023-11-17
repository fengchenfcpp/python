# a1=[23,33,56,-78,97,2,-10,101,-20,120,133,189,231]
# for i in a1:
#     if int(i) % 2 == 0:
#         continue
#     else:
#         print(i)



aa = [23, 33, 56, -78, 97, 2, -10, 101, -20, 120, 133, 189, 231]
aaa = []
for i in aa:
    if i > 0:
        if i % 2 == 1:
            aaa.append(i)
print(aaa)            
print(sum(aaa))        
