# 编写一个返回随机手机号的方法
# import random
# ip1 = ['135','188','150','183']
# ip2 =random.choices('0123456789',k=8)
# print('超哥哥的手机号码;')
# for i in range(1):
#     iphone = random.choice(ip1) + random.choice(ip2)
#     print(iphone)

# import random
# a1 = random.choices(["152","189",""])
# ip1 = ''.join(a1)
# a2 = random.choices('0123456789',k=8)
# ip2 = ''.join(a2)
# print(ip1+ip2)

# def aaa():
#     import random
#     a1 = random.choices(["152","189","188"])
#     ip1 = ''.join(a1)
#     a2 = random.choices('0123456789',k=8)
#     ip2 = ''.join(a2)
#     return ip1 + ip2
# print(aaa())

# 编写一个返回指定长度和内容的随机字符串方法
# import random
# a1 = random.choices('01254638465123456789',k=random.randint(1,20))
# war = ''.join(a1)
# print(war)
# import random
# a1 = random.choices('1234567890',k=4)
# b1 = ''.join(a1)
# print(b1)


# import random
#
# def random_str(str,length):
#     res = random.choices(str,k=length)
#     return ''.join(res)
#
# print(random_str("0123456789qwertyuiopasdfghjklzxcvbnm",4))

# 编写一个返回随机姓名的方法
# import random
# a1=['张','金','李','王','赵']
# a2=['玉','明','龙','芳','军','玲']
# a3=['立','玲','','国',]
# print("超哥哥的结果：")
# for i in range(1):
#  name=random.choice(a1)+random.choice(a2)+random.choice(a3)
#  print(name)

# import random
# a1 = random.choices('张钱金李王',k=1)
# First_name = ''.join(a1)
# a2 = random.choices('玉明龙方芳玲',k=2)
# Last_name = ''.join(a2)
# print(First_name+Last_name)
