list = [13,6,10,21,30,50,4,89,2]
for i in range(len(list)):
	for j in range(i+1,len(list)):
		if list[i]>list[j]:
			list[i],list[j]=list[j],list[i]
print(list)
