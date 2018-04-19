s_acc = "123456"
s_pwd = "abc"
acc = input("请输入一个账号")
pwd = input ("请输入账户密码")
if s_acc == acc and s_pwd == pwd:
	print("登录成功")
elif s_acc == acc and s_pwd > pwd:
	print("密码不对")

elif s_acc > acc and s_pwd == pwd:
	print("账户不对")
