a = []
b = 0
p = []
while b<3:
	x = {}
	c = {}
	c['名字'] = input('请输入名字:')
	if c in p:
		print('姓名重复请重新输入')
		continue
	p.append(c)
	x['年龄'] = input('输入年龄：')
	x['性别'] = input('输入性别：')
	x['qq'] = input('输入qq：')
	x['体重'] = int(input('输入体重:'))
	x.update(c)
	a.append(x)
	b+=1
for i in a:
	print('*'*50)
	for j,v in i.items():
		print('%s:%s'%(j,v))
	print('*'*50)
z = 0
for i in a:
	z+=i['年龄']
print('平均年龄为%0.2f'%(z/len(a)))
