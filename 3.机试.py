def max():
	list1 = []
	list2 = []
	for i in range(5):
		list3 = []
		dict = {}
		while True:
			name = input('输入名字:')
			flag = 0
			for j in list1:
				if name == j['名字']:
					flag = 1
					print('名字重复,重新输入')
			if flag == 0:
				break
		yuwen = float(input('语文成绩:'))
		shuxue = float(input('数学成绩:'))
		yingyu = float(input('英语成绩:'))
		list3.append(yuwen)
		list3.append(shuxue)
		list3.append(yingyu)
		fen = sum(list3)
		jun = fen/3
		dict['名字'] = name
		dict['语文'] = yuwen
		dict['数学'] = shuxue
		dict['英语'] = yingyu
		dict['和'] = fen
		dict['平均'] = jun
		list2.append(fen)
		list1.append(dict)
	max_nu = max(list2)
	for i in list1:
		if max_nu == i['和']:
			print('*'*10)
			print('姓名:%s\n语文成绩:%0.2f\n数学成绩:%0.2f\n英语成绩:%0.2f\n平均成绩:%0.2f\n总分:%0.2f'%(i['名字'],i['语文'],i['数学'],i['英语'],i['平均'],i['和']))
			print('*'*10)
max()
