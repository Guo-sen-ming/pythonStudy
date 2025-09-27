# 抛出异常
# raise Exception("异常")
# raise ValueError("值错误")
# raise TypeError("类型错误")

# raise Exception("这是一个异常提示")
# raise ValueError("这是一个值错误提示")
# raise TypeError("这是一个类型错误提示") 

def error():
  raise ValueError("密码长度不正确")
def login():
  password = input("请输入6位数字密码:")
  print('password是:%s' % password) if len(password) == 6 else error()
def Login():
  try:
    login()
  except ValueError as e:
    print(e)
  print('程序结束')

