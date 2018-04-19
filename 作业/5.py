for a in range(2,101):
	b = 0
	for c in range(1,a+1):
		if a%c==0:
			b+=1
	if b==2:
		print(a)
