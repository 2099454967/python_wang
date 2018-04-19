def city():
	list = [{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
	for i in list:
		for o in i.keys():
			for k in i[o].keys():
				print(o,k,i[o][k])
city()
