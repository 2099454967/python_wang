stus = [{"name":"zhangsan", "age":18},{"name":"lisi", "age":19},{"name":"wangwu", "age":17}]	
stus.sort(key = lambda x:x['name'])
#stus[{'age': 19, 'name': 'lisi'}, {'age': 17, 'name': 'wangwu'}, {'age': 18, 'name': 'zhangsan'}]
print(stus)
stus.sort(key = lambda x:x['age'])
print(stus)
