print('名片系统v1.0版本'.center(30,'*'))
print('1:新增名片'.center(30,' '))
print('2:查找名片'.center(30,' '))
print('3:修改名片'.center(30,' '))
print('4:删除名片'.center(30,' '))
cards = []
while True:
		fun_nuber = int(input('请选择功能'))
		if fun_nuber ==1:
			print('新增')
			flag = 0
			card = {}
			name = input('请输入名字')
			for temp in card:
				if name == temp['name']:
						flag = 1
						break
			if flag == 1:
					print('名字重复了')
					continue
			a = input('请输入职位')
			b = int(input('请输入手机号码'))
			c = input('请输入公司地址')
			d = input('请输入公司名称')
			card['name'] = name
			card['a'] = a
			card['b'] = b
			card['c'] = c
			card['d'] = d
			cards.append(card)
			print('新增成功')
			
