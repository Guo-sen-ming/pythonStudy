str0 = '安逸哟，要下班了'
print(str0.find('下班')) # 5
print(str0, type(str0))
str1 = str0.encode('utf-8')
print(str1, type(str1))
str2 = str1.decode('utf-8')
print(str2, type(str2))

print(str0 == str2)

print('s' in 'str') # True
print('45' not in 'str') # False

a = 1
print(str(a), type(str(a)))

# 切片
b = 'hello'
# print(b[0:2]) # he
# print(b[1:3]) # el
# print(b[:2]) # he
# print(b[2:]) # llo
# print(b[-1]) # o
# print(b[-2]) # l
# print(b[-3:-1]) # ll
# print(b[0::2]) # hlo

print(b.find('x')) # -1
#print(b.index('x')) # ValueError
b = 'jadkawjd'
print(b.count('l')) # 0
print(b.islower()) # True
b = 'asdasd'
print(b.replace('a', 'A', 1)) # Asdasd
b1 = b.replace('a', 'A')
print(b1, 'b1')
b2 = b1.lower()
print(b2, 'b2') 
b3 = b1.upper()
print(b3, 'b3')
b4 = b1.capitalize()
print(b4, 'b4')
print(b.replace('a', 'A', 2)) # AsdAsd
print(b.replace('a', 'A', b.__len__())) # AsdAsd
print(b.__len__())
