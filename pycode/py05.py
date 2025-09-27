# 元组
tupleTest = (1, 2, 3, 4, 5)
print(tupleTest, type(tupleTest))

# 查询
# 查询元素3的索引
tupleTest.index(3)
print(tupleTest.index(3), 'index')
# 查询元素3的个数
tupleTest.count(3)
print(tupleTest.count(3), 'count')
# 判断元素3是否在元组中
print(3 in tupleTest, 'in') # True
# 判断元素3是否不在元组中
print(3 not in tupleTest, 'not in') # False

# 元组的使用场景
# 1. 保存常量
# 2. 保存多个返回值

for i in tupleTest:
  print(i)

tup = [ i for i in (1, 6, 3, 4) ]
print(tup, type(tup)) # [1, 6, 3, 4] <class 'list'>