list = [1,3,5,8,10,20,21,30,34,47,89]
key = 21
center = int(len(list)/2)
if key in list:
	while True:
		if list[center] > key:
			center = center - 1
		elif list[center] < key:
			center = center + 1
		elif list[center] == 21:
			print('要找的数字%d在索引%d'%(key,center))
			break

