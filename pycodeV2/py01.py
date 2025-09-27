# 类
# class Person:
#     height = 180 # 类的属性
#     def run(self): # 实例方法
#         print("run")
#     def change_height(self, height): # 实例方法
#         self.height = height
# # 查看类的属性
# print(Person.height) # 180
# # 新增类的属性
# Person.age = 20
# #print(Person.age) # 20
# # 调用类的方法
# peo = Person()
# peo.run()
# print(peo.height)
# peo.change_height(190)
# print(peo.height)
# print(Person.height)
# print(Person.age)
# print(peo.age)

# class Person:
#     __height = 180 # 私有属性
#     _dog = '旺财' # 受保护属性
#     def __init__(self, name, age) -> None: # 实例化对象自动调用
#         self.name = name
#         self.age = age
#     def __del__(self):
#         print(f"{self.name}对象被销毁")

# peo1 = Person('李四', 'dd')
# peo2 = Person('张三', 20)

# print(peo1.name, peo1.age)
# print(peo2.name, peo2.age)
# # print(Person.__height) # 报错
# # print(peo1.__height) # 报错
# print(peo1._Person__height) # 180
# peo1._Person__height = 200
# print(peo1._Person__height) # 200
# print(peo1._dog) # 旺财
# peo1._dog = '小黑'
# print(peo1._dog) # 小黑
# print(Person._dog) # 旺财
# del peo1
# print(peo2)

# 继承

# class Father:
#     height = 180 # 类的属性
#     _dog = '旺财' # 受保护属性
#     __sex = '男' # 私有属性
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#     def run(self):
#         print("run")
#     def _walk(self):
#         print("walk")
#     def __sing(self):
#         print("sing")

# class Son(Father):
#     def run(self):
#         # super().run()
#         # Father.run(self)
#         super(Son, self).run()
#         print("son run")
# class Grandson(Son):
#     pass

# son = Son('张三', 20)
# grandson = Grandson('李四', 20)
# # print(son.name, son.age) # 张三 20
# # son.run() # run
# # son._walk() # walk
# # # son.__sing() # 报错
# # son._Father__sing() # sing
# # print(son.height) # 180
# # print(son._dog) # 旺财
# # print(son._Father__sex) # 男
# print(grandson.name, grandson.age) # 李四 20
# grandson.run() # run
# grandson._walk() # walk
# grandson._Father__sing() # sing
# print(grandson.height) # 180
# print(grandson._dog) # 旺财
# print(grandson._Father__sex) # 男

# 多父类继承
# class A(object):
#    a = '1'
#    def see(self):
#       print("A see")
# class B(object):
#    b = '2'
#    def see(self):
#       print("B see")
#    def talk(self):
#       print("talk")
# class C(A, B):
#    pass

# print(C.__mro__) # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# qaq = C()
# qaq.see() # A see
# qaq.talk() # talk
# print(qaq.a) # 1
# print(qaq.b) # 2

# 多态
class Animal:
    def talk(self):
        print("talk")
class Dog(Animal):
    def talk(self):
        print("bark")
class Cat(Animal):
    def talk(self):
        print("meow")
def make_talk(animal):
    animal.talk()
dog = Dog()
cat = Cat()
make_talk(dog) # bark
make_talk(cat) # meow