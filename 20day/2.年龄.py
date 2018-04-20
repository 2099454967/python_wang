def age():
	a =int( input('请输入年龄'))
	if a < 2 and a > 0:
		print('婴儿')
	elif a >= 2 and a < 4:
		print('庞珊学步')
	elif a >= 4 and a < 13:
		print('儿童')
	elif a >= 13 and a < 20:
		print('青少年')
	elif a >=20 and a < 65:
		print('成年')
	elif a > 65:
		print('千年王八万年龟')
	else:
		print('输入有误')
age()
