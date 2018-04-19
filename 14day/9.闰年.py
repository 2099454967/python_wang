def run():
	a =int(input('请输入年份'))
	if a%4 == 0 and a%100 !=0:
		print('%d是闰年'%a)
	elif a%400 == 0:
		print('%d是闰年'%a)
	else:
		print('%d是平年'%a)
run()
