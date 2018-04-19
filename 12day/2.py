'''
list = []
name_list = []
count = 0
while True:
	if count == 3:
		break
	dict ={}
	a = input('亲输入名字')
	b = int(input('请输入年龄'))
	c = input('请输入性别')
	d = int(input('请输入qq'))
	e = int(input('请输入体重'))
	if a not in name_list:
		dict['a'] = a
		dict['b'] = b
		dict['c'] = c
		dict['d'] = d
		dict['e'] = e
		list.append(dict)
		name_list.append(a)
		print(list)
		count+=1
	else:
		print('输入重复请重新输入')	
age_sum =0
for a in list:
		age_sum = age_sum+a.get('b')
		print(a)
print('年龄的平均值是%0.2f'%(age_sum/len(list)))
'''
list = []
name_list = []
count = 0
while True:
	if count == 3:
		break
	a = {};
