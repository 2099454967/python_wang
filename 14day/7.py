def hh():
	for i in range(1,10):
		for a in range(1,i+1):
			print('%d*%d=%d'%(a,i,i*i),end = '\t')
		print(' ','\t')
hh()
