account = input('请输入您的账号')
passward = input('请输入您的密码')
nick_name = input('请输入名字')
money = 20000000#原有的存款
need_money = input('请输入您要提取的金额')
sum = money - int(need_money)
print('账号：%s\n密码******\n姓名：%s\n原有的存款：%d\n取款金额%s\n剩余%d'%(account,nick_name,money,need_money,sum))

