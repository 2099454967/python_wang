i = 1
b = 0
c = 0
while i <= 100:
	#1 2 3 4 5 6.....100
	if i%2 == 0: #偶数
		b += i
	else:
		c += i
	i+=1
print('偶数和是%d'%b)
print('奇数和是%d'%c)
