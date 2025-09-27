class Person(object):
    '''我是一个Person类'''
    name = 'leo'
    def __new__(cls):
        print('new')
        return super().__new__(cls)
    def __init__(self) -> None:
        self.age = 18
        print('init')
    def __str__(self) -> str:
        return '嘻嘻哈哈'
    def __call__(self):
        print('call')
    def __len__(self):
        return 10
    def __del__(self):
        print('del')
    def play(self): # 实例方法
        print(f'{Person.name} is playing')
        print(f'age is {self.age}')
    @staticmethod
    def run(): # 静态方法
        print(f'{Person.name} is running')
    @classmethod
    def sleep(cls): # 类方法
        print(f'{cls.name} is sleeping')
peo = Person() # new init
print(len(peo)) # 10
peo() # call  
print(peo.__dict__) # {'age': 18}
print(Person.__dict__) # {'__module__': '__main__', 'name': 'leo', '__new__': <staticmethod(<function Person.__new__ at 0x000001289F9B8EA0>)>, '__init__': <function Person.__init__ at 0x000001289F9B8F40>, 'play': <function Person.play at 0x000001289F9B8FE0>, 'run': <staticmethod(<function Person.run at 0x000001289F9B9080>)>, 'sleep': <classmethod(<function Person.sleep at 0x000001289F9B9120>)>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': '我是一个Person类'}
# 实例方法可以访问类属性和实例属性
# 静态方法不能访问实例属性
# 类方法不可以访问实例属性

# 单例模式
class Singleton(object):
    __adress = None
    def __new__(cls):
        if cls.__adress is None:
            cls.__adress = super().__new__(cls)
        return cls.__adress
s1 = Singleton()
s2 = Singleton()
print(s1 == s2) # True
print(s1._Singleton__adress) # 即使定义成隐藏属性，依然有法子可以访问并修改
print(s2._Singleton__adress)

from py03_test import a as a1
print(a1.__module__) # py03_test
print(a1.__class__) # <class 'py03_test.A'>
print(a1.__dict__) # {}
from py03_test import a as a2
print(a2)
print(a1 == a2) # True

class A:
    '''这是类的一段注释'''
    __doc__ = '啦啦啦'
    pass
print(A.__doc__) # 啦啦啦

def foo():
    '''这是函数的一段注释'''
    pass
print(foo.__doc__) # 这是函数的一段注释

class B(A):
    name = 'leo'
    def __str__(self) -> str:
        return '嘻嘻哈哈'
b = B()
print(b) # 这里会调用__str__方法
print(b.__str__()) # 这里也会调用__str__方法
print(b.name) # 这里不会调用__str__方法

class C:
  def __call__(self):
    print('call')
    return '返回值'
obj_c = C()
obj_c() # call 
print(obj_c()) # call 返回值
print(obj_c.__call__()) # call 返回值

def foo():
    pass
class F:
    pass
f = F()
print(callable(foo)) # True
print(callable(F)) # True
print(callable(f)) # False
