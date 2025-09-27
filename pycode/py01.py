#    print("hello SixStar") 不能缩进
# 这是一个注释
print("hello SixStar")
print("hello SixStar")
print( 'hello SixStar' )
'''
print("hello SixStar")
print("hello SixStar")
print( 'hello SixStar' )
'''
"""
print("hello SixStar")
print("hello SixStar")
print( 'hello SixStar' )
"""
# print('x','y','x',sep='|',end='\n')
# print('a','b','c',sep='@',end='!')

gsm = "456"
gsm = 123
xxx = 123.3
print(gsm + xxx)

gsmType = type(gsm)
print(gsmType)

a = 4 + 3j
print(a)
print(type(a))
print(a + gsm)

str = "123"
str1 = "456"
print(str + str1)

# 格式化
name = "SixStar"
print('你好，我的name是%s' % name)

num = 10
print('num的值是%d,num的类型是%s' % (num,type(num)))
print("num的%34d" % num)

f = 12.34
f1 = 12.3456789
f2 = 112.3456784
print("f的%f,%f,%f" % (f,f1,f2))
print("f的%.2f,%10.2f,%010.7f" % (f,f1,f2))

print("f的%%的%%" % ())

# f格式化
print(f"{name}的值是{num}")
print(f"{name}的值是{num},类型是{type(num)}")

# 运算符
print(10 + 20)
print(10 - 20)
print(10 * 20)
print(10 / 20)
print(10 % 20)
print(10 ** 20)
print(10 // 20)

print('---------------')

# 位运算
print(10 & 20)
print(10 | 20)
print(10 ^ 20)
print(~10)


# const = input("请输入一个常量:")
# print(const)
# print(type(const))

print('dad\nawd')
print('dad\rawd')
print('dad\\nawd')
print('dad\\\nawd')
print('dad\\\\nawd')
print(r'dad\\\\nawd')


