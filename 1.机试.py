list = []
def num():
	for i in range(5):
		dict = {}
		name = input('请输入名字:')
		yuwen = int(input('请输入语文成绩:'))
		shuxue = int(input('请输入数学成绩:'))
		yingyu = int(input('请输入英语成绩:'))
		dict['名字'] = name
		dict['语文成绩'] = yuwen
		dict['数学成绩'] = shuxue
		dict['英语成绩'] = yingyu
		list.append(dict)
		print(list)
	for j in list:
		for j,l in j.items():
			print(j,l)
num()

