'''
name = [1,2,3,4,5,6,7,8,9]
for i in range(len(name)-1,-1,-1):
	name.pop(i)
print(name)
'''

name = [1,2,3,4,5,6,7,8,9]
for i in name[:]:
	name.remove(i)
print(name)

