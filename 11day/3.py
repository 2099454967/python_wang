'''
a = ("武大郎","西门庆","潘金莲","武松","王婆")
b = input('请输入名字')
if b in a:
	print('去捉奸')
else:
	print('下砒霜')
'''
a = ("武大郎","西门庆","潘金莲","武松","王婆")
b = input('请输入名字')
if b not in list(a):
	print('下砒霜')
else:
	print('去捉奸')
