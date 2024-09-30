#!/usr/bin/python
# Filename: xiaomawang2-4.py

import random

number = random.randint(49,51)
running = True
while running:
	if number == 50:
		print ('boom!')
		running = False # this causes the while loop to stop
	elif number != 50:
		print ('no boom!')
		running = False
else:
    print ('结束')