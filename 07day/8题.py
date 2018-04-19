s_acc = "123456"
s_pwd = "123456"
s_mon = 10000
acc = input("请输入账户")
pwd = input("请输入密码")
if s_acc == acc and s_pwd == pwd:
	print("登录成功")
mon = float(input("请输入金额"))
if mon < s_mon:
	print("已取金额:%f,剩余金额:%f"%(mon,s_mon-mon))
elif mon <= s_mon:
	print("没钱取毛线")
else:
	print("非法账户")

