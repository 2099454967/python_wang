height = float(input('请输入身高'))
money = float(input('请输入身价'))
nice = float(input('请输入颜值'))
if (height > 180 and money > 1000000 and nice > 99):
	print("高富帅")
elif (money > 1000000 and nice > 99):
	print('富帅')
elif (nice > 99):
	print('帅')
elif (height > 160 and money < 100 and nice <60):
	print('矮穷挫')

