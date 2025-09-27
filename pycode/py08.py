# 类型转化
# int() float() str() bool()
print(int('123'))
print(float(123))
print(str(123))
print(bool(123))
print(bool(0))
print(bool(''))
print(bool('123'))
print(bool(None))
print(bool(True))
print(bool(False))

# eval()
print(eval('1+2'),type(eval('1+2')))
print(eval("{2, 5, 6}"),type(eval("{2, 5, 6}"))) # {2, 5, 6} <class 'set'>
