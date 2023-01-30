# 未解之謎: a010、
# a001
# print(f"hello, {input()}")

# a002
# a = input().split(" ")
# b = int(a[0])
# c = int(a[1])
# print(b + c)

# a003
# a = input().split(" ")
# b = int(a[0])
# c = int(a[1])
# if (b * 2 + c) % 3 == 0:
#     print("普通")
# elif (b * 2 + c) % 3 == 1:
#     print("吉")
# else:
#     print("大吉")

# a004
# a = int()
# while True:
#     try:
#         a = int(input())
#     except:
#         break
#     if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#         print("閏年")
#     else:
#         print("平年")

# a005
# n = int(input())
# for z in range(1, n + 1):
#     a = input().split(" ")
#     b = int(a[0])
#     c = int(a[1])
#     d = int(a[2])
#     e = int(a[3])
#     if e * c == d * d:
#         a.append(str(int(e * e / d)))
#     else:
#         a.append(str(e + e - d))
#     print(" ".join(a))

# a006
# L = input().split(" ")
# a = int(L[0])
# b = int(L[1])
# c = int(L[2])
# D = b * b - 4 * a * c
# if D < 0:
#     print("No real root")
# elif D == 0:
#     print(f"Two same roots x={int((-b + D ** (1 / 2)) / 2 / a)}")
# else:
#     print(f"Two different roots x1={int((-b + D ** (1 / 2)) / 2 / a)} , x2={int((-b - D ** (1 / 2)) / 2 / a)}")

# a007
# a = int()
# while True:
#     try:
#         a = int(input())
#     except:
#         break
#     p = True
#     for i in range(2, a):
#         if a % i == 0:
#             p = False
#             break
#     if p:
#         print("質數")
#     else:
#         print("非質數")

# a009
# while True:
#     try:
#         a = input()
#     except:
#         break
#     S = []
#     for i in a:
#         S.append(chr(ord(i) - 7))
#     print("".join(S))

# a010 (跳過)
# a = int(input())
# b = a
# L = []
# S = []
# while a != 1:
#     for i in range(2, a + 1):
#         if a % i == 0:
#             L.append(i)
#             a /= i
#             a = int(a)
#             break

# a011
# while True:
#     try:
#         a = input().split(" ")
#     except:
#         break
#     print(len(a))

# a012
# while True:
#     try:
#         L = input().split(" ")
#     except:
#         break
#     a = int(L[0])
#     b = int(L[1])
#     print(abs(b - a))

# g751 2023/01/30
# print("Minecraft")

# c221
# print(2147483640)
# print(9)

# a022
# a = input()
# if a == a[::-1]:
#     print("yes")
# else:
#     print("no")

# a147
# a = 1
# while a != 0:
#     a = int(input())
#     L = []
#     for i in range(1, a):
#         if i % 7 == 0:
#             continue
#         L.append(str(i))
#     print(" ".join(L))

# j408
# h = 0
# m = 0
# s = 0
# n = int(input())
# for i in range(1, n + 1):
#     t = input().split(" ")
#     m += int(t[0])
#     s += int(t[1])
# m += s / 60
# h += m / 60
# m %= 60
# e = ("%2d:%2d" % (h, m))
# print(e.replace(" ", "0"))

# j410
# a = input()
# b = a.count("A")
# c = a.count("C")
# if b>c:
#     print(c)
# else:
#     print(b)

# c418
# a = int(input())
# for i in range(1, a+1):
#     print("*"*i)

# a038
# a = int()
# while True:
#     try:
#         a = input()
#     except:
#         break
#     print(int(a[::-1]))

# a034
# a = int()
# while True:
#     try:
#         a = bin(int(input()))
#     except:
#         break
#     print(a.replace("0b", ""))

# j286
# a = input().split(" ")
# print(int(a[0])+int(a[1])+int(a[2]))

# j324 (WA)
# print(f'Doraemon:"Hi,{input()}!')

# j329
# a = input()
# b = input()
# c = input()
# if c == "yes":
#     print(f"{a}想和{b}絕交")
# else:
#     print(f"{a}不想和{b}絕交")

# j332
# a = input().split(" ")
# b = input()
# c = a.count(b)
# print(c)
# print(int(b)*c)

# j362
# L = []
# a = int(input())
# b = input()
# c = 0
# if b == "print":
#     for i in range(1, a + 1):
#         if a % i == 0:
#             print(i)
#             L.append(i)
# else:
#     for i in range(2, a):
#         if a % i == 0:
#             print(i)
#             L.append(i)
# for i in L:
#     c += int(i)
# print(f"{a}的因數的個數是{len(L)}，{a}的因數的總和是{c}")

# j451
# a = input().split(" ")
# print(int(a[0]) ** int(a[1]))

# j456
# a = int(input())
# b = int(input())
# c = 1
# if a < b:
#     for i in range(1, a + 1):
#         if a % i == 0 and b % i == 0:
#             c = i
# else:
#     for i in range(1, b + 1):
#         if a % i == 0 and b % i == 0:
#             c = i
# print(int(a * b / c))

# d063
# try:
#     1 / int(input())
# except:
#     print(1)
# else:
#     print(0)

# h291
# a = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
#      "December"]
# print(a[int(input()) - 1])

# a020
# d = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 34, "J": 18, "K": 19, "L": 20,
#      "M": 21,
#      "N": 22, "O": 35, "P": 23, "Q": 24, "R": 25, "S": 26, "T": 27, "U": 28, "V": 29, "W": 32, "X": 30, "Y": 31,
#      "Z": 33}
# t = 0
# a = input()
# t += int(d[a[0]]) % 10 * 9 + int(d[a[0]]) // 10
# for i in range(1, 9):
#     t += int(a[i]) * (9 - i)
# t += int(a[9])
# if t % 10 == 0:
#     print("real")
# else:
#     print("fake")

# j430 (放棄)
# a = int(input())
# i = 0
# for i in range(1, a):
#     s = False
#     k = str(i)[0]
#     for j in range(1, len(str(i))):
#         if k != j:
#             continue
#         s = True
#     if s:
#         print(i)

# a008
L = ["零", "壹", "貳", "參", "肆", "伍", "陸", "柒", "捌", "玖", "拾", "佰", "仟", "萬", "億"]
while True:
    try:
        x = int(input())
    except:
        break
    a = x // 100000000
    b = x % 100000000 // 10000
    c = x % 10000
