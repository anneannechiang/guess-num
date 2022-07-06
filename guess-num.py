#使用者設定數字範圍, 系統隨機出 
#讓使用者重覆輸入數字去猜
#猜對, 印出【猜對了！】
#猜錯, 要提示, 比答案大/小

import random
start = input('What is your minimum number ? ')
end = input('What is your maximum number? ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('Guess a number now.. ')
	num = int(num)
	if r == num:
		print('Great Job! You are correct. ')
		print('You only guessed', count, 'times!')
		break
		
	elif r > num:
		print('The number is higher than', num, '!')
	else:
		print('The number is lower than', num, '!')
	print('You have guessed', count, 'times..')





