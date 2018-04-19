abc = float(input('请输入您的身高'))
cd = float(input('请输入您的体重'))
a = (cd/(abc*abc))
if a < 18.5:
	print("过轻")
elif a > 18.5 and a <= 25:
	print('正常')
elif a > 25 and a <= 28:
	print("过重")
elif a > 28 and a <= 32:
	print('肥胖')
elif a >32:
	print('严重肥胖')
