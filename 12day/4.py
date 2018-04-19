print('名片系统v.1版本'.center(30,'*'))
print('增加名片'.center(30,' '))
print('修改名片'.center(30,' '))
print('查找名片'.center(30,' '))
print('删除名片'.center(30,' '))
wq = []
while True:
	fun_number = int(input('请输入功能'))
	if fun_number == 1:
		print('新增')
		flag = 0
		card ={}
		name = input('请输入名字')
		for i in wq:
			if name == i['name']:
					flag = 1
					break
		if flag == 1:
			print('名字重复了')
			continue
		job = input("请输入职位")
		phone = int(input("请输入手机号"))
		company = input("请输入公司名字")
		address = input("请输入公司地址")
		card["name"] = name
		card["job"]  = job
		card["phone"] = phone
		card["company"] = company
		card["address"] = address
		wq.append(card)
		print("新增成功")
		i+=1
