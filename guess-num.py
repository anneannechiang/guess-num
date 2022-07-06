#產生一個隨機整數（1-100) 
#讓使用者重覆輸入數字去猜
#猜對, 印出【猜對了！】
#猜錯, 要提示, 比答案大/小

import random

r = random.randint(1, 4)
count = 0
while True:
	count += 1
	num = input('Guess a number from 1 to 100.. ')
	num = int(num)
	if r == num:
		print('Great Job! You are correct. ')
		print('You only guessed', count, 'times!')
		break
		
	elif r > num:
		print('The number is higher than ', num, '!')
	else:
		print('The number is lower than ', num, '!')
	print('You have guessed', count, 'times..')





