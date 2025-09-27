# 深拷贝与浅拷贝

# 列表
# 浅拷贝
li = [1, 2, 3]
li1 = li
li1.insert(3, 4)
print(li) # [1, 2, 3, 4]
print(li1) # [1, 2, 3, 4]
# 深拷贝
import copy
li = [1, 2, 3, [4, 5]]
li1 = copy.deepcopy(li)
li1[3].append(6)
print(id(li)) # 2951469908352
print(id(li1)) # 2951470042368
print(id(li[3])) # 2951467793472
print(id(li1[3])) # 2951469939264
print(li) # [1, 2, 3, [4, 5]]
print(li1) # [1, 2, 3, [4, 5, 6]]

# 元组 元组由于不能被修改，这里不做讨论
tup = (1, 2, 3)
tup1 = tup
print(id(tup), 'tuple') # 2951469908352
print(id(tup1), 'tuple1') # 2951469908352

# 字典
# 浅拷贝
dict1 = {'name': 'zhangsan', 'age': 18}
dict2 = dict1
dict2['name'] = 'lisi'
print(dict1) # {'name': 'lisi', 'age': 18}
print(dict2) # {'name': 'lisi', 'age': 18}
# 深拷贝
dict1 = {'name': 'zhangsan', 'age': 18}
dict2 = dict1.copy()
dict2['name'] = 'lisi'
print(dict1) # {'name': 'zhangsan', 'age': 18}
print(dict2) # {'name': 'lisi', 'age': 18}
# 深拷贝
import copy
dict1 = {'name': 'zhangsan', 'age': 18}
dict2 = copy.deepcopy(dict1)
dict2['name'] = 'lisi'
print(dict1) # {'name': 'zhangsan', 'age': 18}
print(dict2) # {'name': 'lisi', 'age': 18}

# 集合
# 浅拷贝
set1 = {1, 2, 3}
set2 = set1
print(id(set1)) # 2951469908352
print(id(set2)) # 2951469908352
set2.add(4)
print(set1) # {1, 2, 3, 4}
print(set2) # {1, 2, 3, 4}
# 深拷贝
set1 = {1, 2, 3}
set2 = set1.copy()
set2.add(4)
print(set1) # {1, 2, 3}
print(set2) # {1, 2, 3, 4} 

str1 = '123'
str2 = str1
print(id(str1)) # 2951469908352
print(id(str2)) # 2951469908352
str2 += '4'
print(id(str2)) # 2951469908984 这里修改值的时候数据内存已经发生了变化
print(str1) # '123'
print(str2) # '1234'