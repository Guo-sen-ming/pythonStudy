# os
import os
# os.rename('filetext/01.text', 'filetext/重命名.txt')

# 删除文件
path = 'filetext/重命名.txt'
if os.path.exists(path):
  os.remove(path)
  print('删除成功')
else:
  print('文件不存在')

# 创建文件夹
# os.mkdir('filetext/new1')

# 删除文件夹
# os.rmdir('filetext/new')

# 获取当前目录
print(os.getcwd()) # D:\前端学习\python\code\pycodeV2

# 获取目录列表
print(os.listdir('filetext'))
print(os.listdir())
