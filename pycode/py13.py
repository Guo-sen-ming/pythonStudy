from functools import reduce

print(reduce(lambda x, y: x + y, range(1, 101)))

def num(n):
  if n == 0 or n == 1:
    return 1 
  return num(n-1) + num(n-2)

# print(num(100)) 嵌套太深了，运行不出来


def fei(n):
  li = []
  for i in range(n + 1):
    li.append(num(i))
  return li

lis = fei(10)
print(lis)

# 闭包
def outer(m):
  def inner(n):
    return m + n
  return inner

print(outer(1)(2))

# 装饰器
# def outer(func):
#   def inner(*args, **kwargs):
#     print('inner')
#     func(*args, **kwargs)
#   return inner  
# @outer
# def test(*args, **kwargs):
#   print('test', args, kwargs)
# test('haha', age=18) # inner\ntest ('haha',) {'age': 18}
print('-------------------')
# 多个装饰器
def outer1(func):
  def inner():
    print('outer1', func())
    func()
  return inner

def outer2(func):
  def inner():
    print('outer2', func())
  return inner

@outer1
@outer2
def test():
  return 'test'
test() # outer2 test\outer1 None\outer2 test