# 变量作用域 def class lambda
# 变量搜索规则 ：就近原则
# 局部变量，无法在外部使用
# global 在全局作用域中申明全局作用域的变量
# c = 999
# def ccc():
#     global c
#     c = 888
# ccc()
# print(c)

# 变量引用赋值
# python中变量赋值是对存储空间的引用，而不是对存储空间的拷贝

# 字符串
# a = '1234567890'
# b = '456'
# print(a+b)
# print(a*5)
# print(a[0])
# print(a[2:-1])
# print(a[4:])
# print(a[:-2])

# # 空格
# a = ' qwetytuiobjki '
# a = a.strip()
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())
# # 替换
# line = '用户名，金额,账户'
# line = line.replace('，',',')
# print(line)
# # 切片
# print(line.split('，'))

# 列表

# 遍历列表
l = [1,2,3,4,5,6,7,8,9,0]
for i in l
    print(i)
# 元组

# 集合
s = set()
# 遍历
# 不支持下标索引，所以不支持其它操作

# 字典
