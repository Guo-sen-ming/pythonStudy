# 程序跑起来就是一个进程，一个进程包含多个线程
# 进程状态：就绪、运行、阻塞

import time

print('进程开始')
time.sleep(2)
print('进程结束', time.time())