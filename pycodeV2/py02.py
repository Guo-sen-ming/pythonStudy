# 类的静态方法
# 类的类方法
class Person:
    state = 'good'
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    @staticmethod
    def run(): # 静态方法
        print("run")
    def eat(self): # 实例方法
        print("eat")
    @classmethod
    def change_state(cls, state):
        cls.state = state
        cls.run()
peo = Person('张三', 20)
print(peo.state) # good
peo.change_state('bad') # run
print(peo.state) # bad
peo.run() # run
Person.run() # run
# Person.change_height(180) # 报错

# 静态方法能被继承吗？ 可以的
class Student(Person):
    def run(self):
        super().run()
        print("Student run")
stu = Student('李四', 20)
stu.run() # run Student run

