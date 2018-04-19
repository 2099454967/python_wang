print('名片系统v1.0系统'.center(30,'*'))
print('1:增加名片'.center(30,' '))
print('2:查找名片'.center(30,' '))
print('3:修改名片'.center(30,' '))
print('4:删除名片'.center(30,' '))
print('5:退出系统'.center(30,' '))
cards =[]
while True:
		fun_number =int(input('请输入功能:'))
		if fun_number ==1:
				flag =0
				card = {}

				name =input('请输入名字:')
				for i in cards:
						if name == i['name']:
								flag =1
								break
				if flag ==1:
					print('名字重复了')
					continue
				job = input('请输入职位:')
				phone = int(input('请输入手机号:'))
				company = input('请输入公司名称:')
				adderss = input('请输入公司地址:')
				card['name'] = name
				card['job'] = job
				card['phone'] = phone
				card['company'] = company
				card['adderss'] = adderss
				cards.append(card)
				print('新增成功')
				break

					
