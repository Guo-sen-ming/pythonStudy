# 用户从控制台输入成绩：如果满分，输出你真棒！如果60分，输出”还要继续加油哈！
# score = input("请输入成绩:")
# score = int(score)
# print(score)
# if score == 100 or score > 90:
#     print("你真棒！")
# elif (score <= 60):
#     print("还要继续加油哈！")
# else:
#     print("成绩有误！")

# print( not score)

# print(int(False))

# print(int(3>2))

# print(int(3 + 4.3))

# print(int("123.2"))

# 三目运算

# a = 10
# b = a + 1 if type(a) == int else a - 1
# print(b)

# print( 2 < b < 10 )

# a = 11
# print(10 < a < 19)

# 循环
# 帮我用while循环写一个斐波那契数列
# 斐波那契数列：从 0, 1 开始，后一个数是前两个数之和
# n = 10  # 要打印的项数
# a, b = 0, 1
# count = 0
# while count < n:
#     print(b)
#     a, b = b, a + b
#     count += 1

# a = 10
# while a > 0:
#     print(a)
#     a -= 1
#     if a == 5:
#       break

for i in range(0, 10, 2):
    print(i, end='  ')

print()

ans = 0
for i in range(1, 101):
    ans += i
print(ans)
