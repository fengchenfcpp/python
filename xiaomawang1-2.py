#!/usr/bin/python
# Filename: xiaomawang1-2.py
answer = 'yes'
running = True
while running:
	guess = str(input('Print? : '))
	if guess == answer:
		print ('我爱python')
		running = False # this causes the while loop to stop
	elif guess != answer:
		print ('需要输入yes')

else:
    print ('结束')
