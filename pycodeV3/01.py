# 进程与线程

# 导入线程模块
from threading import Thread
# 创建共享资源
li = []
# 导入时间模块
import time

# 写入数据
def write_data():
  for i in range(5):
    li.append(i)
    time.sleep(1)
    print('写入数据', li)
# 读取数据
def read_data():
  for i in li:
    print('读取数据', i)
    time.sleep(1)

if __name__ == '__main__':
  # 创建线程
  t1 = Thread(target=write_data)
  t2 = Thread(target=read_data)
  # 启动线程
  t1.start()
  # 等待线程执行完毕 ，等待t1线程执行完毕后，再执行t2线程
#   t1.join()
  time.sleep(5.1)
  t2.start()
  # 等待t2线程执行完毕
#   t2.join()
