# print("hello_world")
# a 变量 =赋值符 值
# a="hello_world"
# print(a)
'''
字符串 '' "" ''' ''' """ """
number 整数 小数 复数 Comples
布尔值 True Fslse
空值 None

存多个数据
列表 list [1,2,3,4,7,6,5]  可修改 访问速度慢 空间占比大 有序
元组 tuple （1,2,3,4）  不可修改 访问速度快  空间占比小  有序
集合 set {1,2,3} 不可重复 无序

字典 dict # key 不可修改（元组）key 不可重复（集合） 无序
'''

# l = [1,2,3,4,5,6]
# print(l[0])
#
# t = (1,2,3,4,5,6)
# print(t[2])
#
# s = {1,2,3,4,5,6}
# print(s)

# 类型转换
#
# a = 2
# b ='3'
# print(a + int(b))
# print(str(a) + b)
#
# a = 2
# b = '3.3'
# print(a + float(b))
# print(str(a) + b)
#
# a = True
# b = '3.3'
# print(a+float(b))
# print(str(a) + b)
#
# l = [1,2,3,4,5,6]
# print(tuple(l))
# print(set(l))
#
# t = (1,2,3,4,5,6)
# print(list(t))
# print(set(t))
#
# s = {1,2,3,4,5,6}
# print(list(s))
# print(tuple(s))
#
# a = "1,2,3,4,5,6"
# print(list(a))
# print(tuple(a))
# print(set(a))

# 运算符
'''
# 成员运算符
'''
'''
a = "a,b,c,d"
l = ["a","b","c","d"]
t = ("a","b","c","d")
s = {"a","b","c","d"}
d = {"name":"张三","sex":"男"}

print("a" in a)
print("a" in l)
print("a" in t)
print("a" in s)
print("name" in d)
'''
'''
money = 100000000
if (money >= 100000000):
    print("我晓天吃翔！你一坨，我一坨！")
else:
    print("我越吃翔！你一坨，我一坨！")
'''
'''
money = 10000000
if (money < 1000):
    print("洗洗睡吧！")
elif(money < 10000):
    print("吃个包子，吃个馒头！")
elif(money < 100000):
    print("吃个包子，吃个馒头，吃个鸡腿！")
elif(money < 1000000):
    print("吃个包子，吃个馒头，吃个鸡腿，吃个猪肘子！")
else:
    print("和杨幂一起吃包子，馒头，鸡腿和猪肘子！")
'''
'''
# 循环
for i in range(10000):
    print("陈独秀，请坐下！")
for i in range (100):
    print(i)
'''
# print(list(range(100)))
# print(tuple(range(1,10,3)))
# print(tuple(range(80,1,-8)))
# print(tuple(range(1000,1,-1)))
#
# while False :
#     print("hellp")

# for i in  range(20):
#     if(i in (5,7)):
#         continue
#     print(i)
s = 0
for i in range(1,101):
    s += i
    print(s)