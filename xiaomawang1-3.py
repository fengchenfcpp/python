#!/usr/bin/python
# Filename: xiaomawang1-2.py
<<<<<<<< HEAD:xiaomawang1-3.py
for i in range(1, 5):
	print (i)
	print ('这是第',i,'次, 我真棒')
========
answer = 'yes'
running = True
while running:
	guess = str(input('Print? : '))
	if guess == answer:
		print ('我爱python')
		running = False # this causes the while loop to stop
	elif guess != answer:
		print ('需要输入yes')

>>>>>>>> f12224e7cea7ba928ae8d1deed97ea1b60323531:xiaomawang1-2.py
else:
    print ('结束')
