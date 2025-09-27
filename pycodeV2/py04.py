# 文件

# f = open('py04_test.txt', mode='r+', encoding='utf-8')
# print(f.read()) # '加油 gogogo'
# print(f.read(5)) # '加油 g
# print(f.readline()) # '加油 gogogo'
# print(f.readline()) # '黑咖啡品味有多浓'
# print(f.readlines()) # ["'加油 gogogo'\n", "'黑咖啡品味有多浓'\n", '\n', "'我只要汽水的轻松'"]
# f.write('写入')
# print(f.readline()) # 16
# f.write('22')
# print(f.mode) # r
# print(f.name) # py04_test.txt
# print(f.closed) # False
# f.close()
# print(f.closed) # True

# f1 = open('py04_test1.txt', mode='a+', encoding='utf-8')
# if f1.tell():
#   f1.seek(0, 0)
# if f1.read():
#   f1.write('\n追加新的内容bbb')
#   print('追加成功！')
# else:
#   f1.write('写入aaa')
#   print('写入成功！')
# f1.close()

# 

# 案例 复制图片
with open('images/test.png', mode='rb') as png:
  with open('images.txt', mode='a+', encoding='utf-8') as image:
    image.seek(0, 0)
    if image.read() == '':
      image.write(str(png.read()))
      print(image.tell())
    else:
      print('文件已存在')
  path = 1
  while True:
    with open(f'images/test{path}.png', mode='ab+') as png1:
      png1.seek(0, 0)
      png1HasData = bool(png1.read())
      print(png1HasData)
      if not png1HasData:
        png1.write(png.read())
        break
      else:
        path += 1
