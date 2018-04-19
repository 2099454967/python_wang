import random
a = random.randint(1,100)
for b in range(1,11):
	c = int(input('请输入数字:'))
	if c<a:
		print('猜小了')
	elif c>a:
		print('猜大啦')
	else:
		print('猜对了')
		break 
	

