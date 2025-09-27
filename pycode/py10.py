# 函数
def test(*args):
  sum = 0
  #print(args)
  for i, v in enumerate(args):
    if (i == len(args) - 1) :
      print(v, '=', end = ' ')
    else:
      print(v, '+', end = ' ')
    sum += v
  return sum

# sum = test(1, 1)
# print(sum) # 3
# sum1 = test(1)
# print(sum1) # 11
# sum2 = test()
# print(sum2) # 0
# sum3 = test(1, 2, 3)
# print(sum3) # 6
# sum4 = test(1, 2, 3, 4)
# print(sum4) # 10


# def fun():
#   global a,b
#   a = 1
#   b = 3
#   print(a) # 1
# global a,b
# # a = 0
# # b = 1
# fun()
# print(a, b) # 1

# # nonlocal 作用: 在函数嵌套中修改外层函数的变量
# def fun1():
#   a = 1
#   def fun2():
#     nonlocal a
#     a = 2
#     print(a) # 2
#   fun2()
#   print(a) # 2
# fun1()

# # lambda
# # 匿名函数
# fun = lambda x,y: x + y if x > y else x - y
# print(fun(1, 2)) # 3

# 查看内置函数
# 大写字母是内置常量名。小写字母是内置函数名
# print(dir(__builtins__))

print(sum([1, 2, 3])) # 6
print(min(-1, -2, key=abs)) # -1

# zip()
print(zip(), type(zip())) # <zip object at 0x000002182FADF880> <class 'zip'>
print(list(zip([1, 2, 3], ['a', 'b', 'c'], ['x', 'y', 'z']))) # [(1, 'a', 'x'), (2, 'b', 'y'), (3, 'c', 'z')]

# map()
print(map(lambda x: x + 1, [1, 2, 3]), type(map(lambda x: x + 1, [1, 2, 3]))) # <map object at 0x000002182FADF880> <class 'map'>
print(list(map(lambda x: x + 1, [1, 2, 3]))) # [2, 3, 4]

# reduce() 作用: 对列表中的元素进行累积操作
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3])) # 6
print(reduce(lambda x, y: x + y, [1, 2, 3], 10)) # 16
print(type(reduce(lambda x, y: x + y, [1, 2, 3], 10))) # 16 <class 'int'>
# 通过reduce函数写斐波拉契数列

# 使用 reduce 计算第 n 个斐波那契数（n 从 1 开始计数：F1=0, F2=1）
def fib_n(n: int) -> int:
  if n <= 0:
    return 0
  # 以 (0,1) 作为种子，每次把 (a,b) 映射到 (b, a+b)，迭代 n-1 次，取第一个数
  return reduce(lambda p, _: (p[1], p[0] + p[1]), range(n - 1), (0, 1))[0]

# 使用 reduce 生成前 n 个斐波那契数的列表
def fib_list(n: int) -> list[int]:
  if n <= 0:
    return []
  # 从 [0,1] 开始，累计把下一个数追加到列表尾部
  return reduce(lambda acc, abb: acc + [acc[-1] + acc[-2]], range(max(0, n - 2)), [0, 1])[0:1]

# 示例演示
print(fib_n(1))   # 0
print(fib_n(2))   # 1
print(fib_n(10))  # 34

print(fib_list(1))   # [0]
print(fib_list(2))   # [0, 1]
print(fib_list(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print([0,1] + [2, 3]) # [0, 1, 2, 3]

# 拆包
print(*[1,2,3])
li = {1,2,3}
# a,b,c = li
a, *b = li
print(a,b) # 1 [2, 3]
