def jisuanji(x,y,a):
	if a == '+':
		z = x+y
		print('和是%.02f'%z)
	elif a == '-':
		z = x-y
		print('差是%.02f'%z)

	elif a == '*':
		z = x*y
		print('积是%.02f'%z)
		
	elif a == '/':
		z = x/y
	
		if y !=0:
			print('商是%.02f'%z)
	else:

		print('输入错误')
while True:
	x = float(input('请输入数字'))
	y = float(input('请输入数字'))
	z = input('请输入符号')
	jisuanji(x,y,z)
