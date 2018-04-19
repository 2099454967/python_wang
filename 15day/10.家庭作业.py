
print('学生成绩管理'.center(30,"*"))
print('1:录入成绩'.center(30," "))
print('2:查询成绩'.center(30," "))
print('3:修改成绩'.center(30," "))
print('4:删除成绩'.center(30," "))
print('5:打印成绩'.center(30," "))
print('6:退出系统'.center(30," "))

cards = []
while True:
	fun_number = int(input('请输入功能'))
	if fun_number ==1:
		print('新增')
		flag = 0
		card = {}
		student_number = int(input('请输入学号:'))
		for temp in cards:
			if student_number == temp['学号']:
				flag = 1
				break
		if flag == 1:
			print('名字重复了')
			continue
		name = input('请输入名字:')
		yuwen = float(input('请输入语文分数:'))
		shuxue = float(input('请输入数学分数:'))
		yinyu = float(input('请输入英语分数:'))
		diannao = float(input('请输入电脑分数:'))
		card['学号'] = student_number
		card['姓名'] = name
		card['语文成绩'] = yuwen
		card['数学成绩'] = shuxue
		card['英语成绩'] = yinyu
		card['电脑成绩'] = diannao
		#放到列表中
		cards.append(card)
		print('新增成功\n')
	elif fun_number ==2:
		student_number = int(input('请输入要查的学号:'))
		flag = 0
		for temp in cards:
			if student_number == temp['学号']:
				flag = 1
				for j,v in temp.items():
					print('%s:%s'%(j,v))
				break
			if flag == 0:
				print('查无此人')
	elif fun_number == 3:
		student_number = int(input('请输入要修改的学号:'))
		for temp in cards:
			if student_number == temp['学号']:
				print("1:修改名字")
				print("2:修改语文成绩")
				print("3:修改数学成绩")
				print("4:修改英语成绩")
				print("5:修改电脑成绩")
				new_num = int(input('请输入你要修改的序号:'))
				if new_num ==1:
					new_name = input('请输入新的名字:')
					temp['name'] = new_name
				elif new_num == 2:
					new_yuwen = input('请输入新的语文成绩:')
					temp['yuwen'] = new_yuwen
				elif new_num == 3:
					new_shuxue = input('请输入新的数学成绩:')
					temp['shuxue'] = new_shuxue
				elif new_num ==4:
					new_yinyu = input('请输入新的英语成绩:')
					temp['yinyu'] = new_yinyu
				elif new_num ==5:
					new_diannao = input('请输入新的电脑成绩:')
				else:
					print('输入有误\n')
	elif fun_number == 4:
		student_number = int(input('请输入要删除的学号'))
		flag = 0
		for temp in cards:
			if student_number == temp['学号']:
				flag = 1
				cards.remove(temp)
				print('删除成功')
				break
				
			else:
				print('没有此人')
	elif fun_number == 5:
		#print('学号\t名字\t语文成绩\t数学成绩\t英语成绩\t电脑成绩')
		#$for i in cards:
			#print('%d\t%s\t%0.2f\t%0.2f\t%0.2f\t%0.2f\t'%(i['学号'],i['姓名'],i['语文成绩'],i['数学成绩'],i['英语成绩'],i['电脑成绩']))
			print("学号".center(8," "),end=' ')
			print("名字".center(8," "),end=' ')
			print("语文成绩".center(8," "),end=' ')
			print("数学成绩".center(8," "),end=' ')
			print('英语成绩'.center(8,' '),end=' ')
			print('电脑成绩'.center(8,' '))
			for temp in cards:
				print(str(temp['学号']).center(10," "),end=' ')
				print(temp['姓名'].center(10," "),end=' ')
				print(str(temp['语文成绩']).center(12," "),end=' ')
				print(str(temp['数学成绩']).center(12," "),end=' ')
				print(str(temp['英语成绩']).center(12," "),end=' ')
				print(str(temp['电脑成绩']).center(12," "))
