# 资源竞争
# 多个线程同时访问共享资源，可能会导致资源竞争问题
# 解决方法：使用锁机制，确保每个线程在访问共享资源时，只有一个线程可以访问
from threading import Thread, Lock
import time

a = 0
b = 10000000

# def add1():
#   global a
#   for i in range(b):
#     a += 1
#   print('add1', a)

# def add2():
#   global a
#   for i in range(b):
#     a += 1
#   print('add2', a)

# add1()
# add2()

# 创建互斥锁
lock = Lock()

def add1():
  global a
  lock.acquire()
  for i in range(b):
    a += 1
    # 解锁
  lock.release()
  print('add1', a)

def add2():
  global a
  # 加锁
  lock.acquire()
  for i in range(b):
    a += 1
# 解锁
  lock.release()
  print('add2', a)

if __name__ == '__main__':
  # 创建线程
  t1 = Thread(target=add1)
  t2 = Thread(target=add2)
  # 启动线程
  t1.start()
  # 等待线程执行完毕 ，等待t1线程执行完毕后，再执行t2线程
#   t1.join()
  t2.start()
  # 等待t2线程执行完毕
#   t2.join()