# 生成器
set = (1, 2, 3, 4, 5)
print(set)
li = [i + 1 for i in set]
print(li)
gen = (i + 1 for i in set)
print(gen) # <generator object <genexpr> at 0x000001482C2435E0>
print(next(gen)) # 2

# 生成器函数
li = []
def gen_func(n):
  for i in range(1,n+1):
    li.append(i)
    yield i
gen = gen_func(5)
gen2 = gen_func(9)
# print(gen) # <generator object gen_func at 0x000002025D294B40>
# print(next(gen)) # 1
# print(next(gen)) # 2
# print(next(gen)) # 3
# print(li)

# for i in gen: # 在内部已经调用了next()方法
#   pass

for i in gen2:
  pass

print(li) # [1, 2, 3, 4]

# change 测试git