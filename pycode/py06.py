# 字典
# 定义
# 1. 使用花括号
dict1 = {'name': 'zhangsan', 'age': 18}
print(dict1, type(dict1))
# 2. 使用dict()函数
dict2 = dict(name='lisi', age=19)
print(dict2, type(dict2))
# 3. 使用zip()函数
dict3 = dict(zip(['name', 'age'], ['zhangsan', 18]))
print(dict3, type(dict3))
# 4. 使用**运算符
dict4 = dict(**{'name': 'wangwu', 'age': 20})
print(dict4, type(dict4))

# 字典的特点
# 1. 无序
# 2. 可变
# 3. 键值对

# 示例字典后续都使用这个字典做示例
dictTest = {'name': 'zhangsan', 'age': 18}

# 查
# # 1. 使用[]
# print(dictTest['name']) # zhangsan
# # 2. 使用get()
# print(dictTest.get('age')) # 18
# # 3. 使用in
# print('name' in dictTest) # True
# # 4. 使用keys()
# print(dictTest.keys()) # dict_keys(['name', 'age'])
# # 5. 使用values()
# print(dictTest.values()) # dict_values(['zhangsan', 18])
# # 6. 使用items()
# print(dictTest.items()) # dict_items([('name', 'zhangsan'), ('age', 18)])

# 改
# # 1. 通过键名修改
# print(dictTest['name']) # zhangsan
# dictTest['name'] = 'lisi'
# print(dictTest['name']) # lisi
# # 2. 使用update()
# dictTest.update({'name': 'wangwu'})
# print(dictTest['name']) # wangwu

# # 增
# # 1. 通过键名添加
# dictTest['sex'] = '男'
# print(dictTest) # {'name': 'wangwu', 'age': 18, 'sex': '男'}
# # 2. 使用update()
# dictTest.update({'aa': 'bb'})
# print(dictTest) # {'name': 'wangwu', 'age': 18, 'sex': '男', 'aa': 'bb'}

# 删
# 1. 使用del
# del dictTest['name']
# print(dictTest) # {'age': 18}
# 2. 使用pop()
# dictTest.pop('age')
# print(dictTest) # {}
# 3. 使用popitem()
# print(dictTest)
# dictTest.popitem()
# print(dictTest) # {'name': 'zhangsan'}
# 4. 使用clear()
# dictTest.clear()
# print(dictTest) # {}

for i in dictTest:
  print(i)

for i in dictTest.values():
  print(i)

for i in dictTest.items():
  print(i)

values = dictTest.values()
print(values[0])