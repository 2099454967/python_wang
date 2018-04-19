def jieguo(x,y,fuhao):
	if fuhao == '+':
		return x+y
	elif fuhao == '_':
		return x-y
	elif fuhao == '*':
		return x*y
	elif fuhao == '/':
		if y != 0:
			return x/y
		else:
			print('输入错误')
	elif fuhao == '**':
		return x**y
	else:
		print('输入错误')
while True:
	x = float(input('请输入数字'))
	y = float(input('请输入数字'))
	fuhao = input('请输入符号')
	jieguo = jieguo(x,y,fuhao)
	print(jieguo)
