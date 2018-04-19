a = {"姓名":"王保辉","年龄":18,"性别":"男"}
print(a)
#添加值
a['名族'] = '汉'
a['地址'] = '山东'
print(a)
#删除指定的值
a.pop('地址')
#修改指定的值
a['姓名'] = '王保轩'
print(a)
#可以从字典中取值,不会报错
print(a.get('性别'))
print(a)
#合并a和a2的值
a2 = {'name':'王保轩','地址':'山东'}
a.update(a2)
print(a)
#删除指定的值
a.pop('name')
print(a)
#所以的键
print(a.keys())
#所以的值
print(a.values())
#所以键和值的元组列表
print(a.items())
