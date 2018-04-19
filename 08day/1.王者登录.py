s_acc = 123456
s_pwd = 123456
a = 1
while True:
	acc = int(input('请输入账号'))
	pwd = int(input('请输入密码'))

	if s_acc == acc and s_pwd == pwd:
		a = int(input('0 = ADC 1 = 肉　3 = 法师:'))
		if a == 0:
			print('鲁班大师')
		elif a == 1:
			print('程咬金')
		elif a == 3:
			print('王邵君')
		break
	else:
		print('错误%d次'%a)
	a+=1
	if a == 4:
		print('账户被封')
		break


