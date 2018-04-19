a = ['张三','李四','王二麻']
for i in a:
	print('%s请您和我一起共进晚餐'%i)

print('%s因病无法和您共进晚餐'%a[0])
a[0] = '观音'
for i in a:
	print('%s请您和我一起共进晚餐'%i)

print('因为我有个比较豪华的包间')
a.insert(0,'张飞')
a.insert(3,'刘备')
a.append('鲁班')
for i in a:
	print('%s请您和我共进晚餐'%i)

print('因为餐桌不够只能邀请两位嘉宾了')
for i in a:
	print('%s你别来了桌子不够大'%a[0:5])
