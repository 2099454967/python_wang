def su():
	for i in range(100,201):
			a =0
			for b in range(1,i+1):
					if i % b == 0:
							a+=1
			if a == 2:
					print(i)
su()
