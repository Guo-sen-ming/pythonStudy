# 集合
# 定义
# setTest = {1, 2, 'd', 4, 5}
# print(setTest, type(setTest))
# setTest1 = {}
# print(setTest1, type(setTest1))
# setTest2 = set()
# print(setTest2, type(setTest2))
# setTest3 = set([1, 2, 3, 4, 5])
# print(setTest3, type(setTest3))
# setTest4 = set(range(1, 6))
# print(setTest4, type(setTest4))
# setTest5 = set('12345')
# print(setTest5, type(setTest5))

# 特点
# 1. 无序
# 2. 不可变
# 3. 无重复
# li = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# tup = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
# newli = list(set(li))
# print(newli) # [1, 2, 3, 4, 5]
# newtup = tuple(set(tup))
# print(newtup) # (1, 2, 3, 4, 5)

# 集合的常见操作
# 集合示例

setTest = {1, 2, 3, 4, 5}
# 增
# setTest.add(6)
# print(setTest) # {1, 2, 3, 4, 5, 6}
# dict = { 'name': 'aa', 'age': 18 }
# setTest.update(dict)
# print(setTest) # {1, 2, 3, 4, 5, 'name', 'age'}
# 删
# setTest.remove(5)
# print(setTest) # {1, 2, 3, 4}
# setTest.discard(2)
# print(setTest) # {1, 3, 4, 5}
# pop是随机删除，不能指定删除，因为集合是无序的
# setTest.pop()
# print(setTest) # {2, 3, 4, 5}
# strSet = {4,5,6,7,8,1}
# print(strSet) # {0, 1, 2, 3, 4}
# strSet.pop()
# print(strSet) # {'2', '3', '4', '5'}
# setTest.clear()
# print(setTest) # {}
# 改

# 查
# print(6 in setTest) # True
# print(6 not in setTest) # False

# 集合的交集和并集
setTest1 = {1, 2, 3, 4, 5}
setTest2 = {4, 5, 6, 7, 8}
print(setTest1 & setTest2) # {4, 5}
print(setTest1 | setTest2) # {1, 2, 3, 4, 5, 6, 7, 8}
print(setTest1.intersection(setTest2)) # {4, 5}
print(setTest1.union(setTest2)) # {1, 2, 3, 4, 5, 6, 7, 8}
