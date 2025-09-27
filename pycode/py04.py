# 列表
# list1 = [1, 2, 3, 1, 4, 5]
# print(list1)
# print(type(list1))

# list2 = list(range(1, 6))
# print(list2)
# print(type(list2))

# list3 = [1, 'a', 3.14, True]
# print(list3)
# print(type(list3))

# 列表的新增方法
# append() 在列表末尾添加一个元素
# list1.append(6)
# print(list1)
# insert() 在列表指定位置插入一个元素
# list1.insert(0, 0)
# print(list1)
# extend() 在列表末尾添加多个元素
# list1.extend([6, 7, 8])
#list1.extend('123')
# list1.extend(range(6, 9))
# print(range(6, 9), type(range(6, 9)))
# print(list1)
# 在列表开头通过insert()添加1个元素
# list1.insert(0, 1)
# print(list1)
# 在列表末尾通过insert()添加1个元素
# list1.insert(len(list1), 10)
# print(list1)

# 列表的删除方法
# remove() 删除列表中第一个匹配的元素
# print(list1, 'before remove')
# list1.remove(1)
# print(list1)
# # pop() 删除列表中指定位置的元素
# list1.pop(-1)
# print(list1)
# # del 删除列表中指定位置的元素
# del list1[3]
# print(list1)
# # 删除列表中多个元素
# print(list1, '******')
# del list1[0:2]
# print(list1)


# 查找列表中的元素
# 定义一个列表保存用户的name,用户输入名字，需要判断名字是否在列表中，如果在列表中，输出"在列表中"，否则输出"不在列表中"
# name_list = ['zhangsan', 'lisi', 'wangwu']
# while True:
#   name = input('请输入名字: ')
#   if name in name_list:
#     print('在列表中,请重新输入')
#   else:
#     print('不在列表中')
#     name_list.append(name)
#     print(name_list)
#     break

# arr = list(range(1, 6))
# del arr
# print(arr, type(arr)) # NameError: name 'arr' is not defined

# 列表的排序
# print(list1, 'before sort')
# list1.sort()
# print(list1)

# print(list1, 'before sort')
# list1.sort(reverse=True)
# print(list1)

# print(list1, 'before reverse')
# list1.reverse()
# print(list1)

# 遍历列表
# 方法1
for i in [4, 5, 6]:
  print(i)
# 方法2
[ print(i, '2', end='\t') for i in [4, 5, 6] ]

# 列表推导式
listTest = [i for i in range(1, 6)]
print(listTest) # [1, 2, 3, 4, 5]
listTest = [i for i in range(1, 6) if i % 2 == 0]
print(listTest) # [2, 4]
