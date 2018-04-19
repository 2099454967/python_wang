s_acc = 123456
s_pwd = 123456
acc = int(input('请输入账号'))
pwd = int(input('请输入密码'))
if acc == s_acc and pwd == s_pwd:
	print('欢迎进入王者荣耀')
else:
	print('密码或账户错误')

