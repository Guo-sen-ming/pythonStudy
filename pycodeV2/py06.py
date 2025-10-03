# 可迭代对象

# 判断是否为可迭代对象
# a = { 'name': '张三', 'age': 20 }

# print(isinstance(a, dict))

# # from collections import Iterable # 仅适用于3.3之前的版本
# from collections.abc import Iterable
# print(isinstance(a, Iterable))
# s = 'xxx'
# print(isinstance(s, (int, list))) # False
# print(isinstance(s, (str, list))) # True

# li = [1, 2, 3, 4]
# li1 = iter(li)
# print(li.__iter__(), 'xxx')
# print(li1)
# print(next(li1))
# print(next(li1))
# print(next(li1))
# print(next(li1))
# print(next(li1))

# 自定义迭代器类
from collections.abc import Iterator
class MyIterator(object):
  def __init__(self):
    self.num = 10
  def __iter__(self):
    return self
  def __next__(self):
    if self.num >= 0:
      current = self.num
      self.num -= 1
      return current
    else:
      raise StopIteration

te = MyIterator()
# te1 = iter(te)
# print(next(te1))
# print(next(te1))
# print(next(te1))
# print(next(te1))
# print(next(te1))
# print(next(te1))
# print(next(te1))
# print(next(te1))
# print(next(te1))
# print(next(te1))
# print(next(te1))
print(isinstance(te, Iterator)) # True

for i in te:
  print(i)
