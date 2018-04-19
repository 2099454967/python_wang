print("名片系统v1.0版本".center(30,"*"))
print("1:名片增加".center(30,"*"))
print("2:名片修改".center(30,"*"))
print("3:名片查找".center(30,"*"))
print("4:名片删除".center(30,"*"))
cards = []
while True:
	fun_number = int(input('请输入功能'))
	if fun_number == 1:
		flag =0
		card={}
		name = input('请输入名字')
		for temp in cards:
			if name == temp['name']:
				flag =1
				break
		if flag ==1:
			print('名字重复了')
			comtinue
		job = input("请输入职位")
		phone = int(input('请输入手机号'))
		company = input('请输入公司名称')
		address = input('请输入公司地址')
		cards.append(card)
		print('新增成功')
	elif fun_number ==2:
		name =input('请输入要查名字')
		flag =0
		count =0
		for temp in cards:
				count+=1
				if name == temp['name']:
						flag = 1
						break
		if flag == 0:
			print('查无此人\n')
		else:
				print('姓名:%s\n职位:%s\n手机号:%s\n公司:%s\n地址:%s'%(cards[count-1]["name"],cards[count-1]["job"],cards[count-1]["phone"],cards[count-1]["company"],cards[count-1]["address"]))
'''
	elif fun_number == 3:
		print("修改")
'''
		elif fun_number == 4:
			name = input('请输入您要删除的名字')
			flag =1
			sure_num = int(input('0确认 1返回'))
			if sure_num == 0:
					cards.remove(temp)
					print('删除成功')
			break

