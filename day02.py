# # 除法运算
# #   被除数不能为0
# '''
# 函数（方法）————————def div(a,b):
# def 定义方法关键字————define v. 给（词语）下定义
# div 方法名————
# a,b 用来接收外界参数，参数必须写到括号里面
# (a,b) 整体被称为参数列表
# : 冒号表示下方包含一个代码块（方法体）
# '''
# # def div (a,b):
# #     if b == 0:
# #         print("被除数不能为0")
# #     else:
# #         print(a / b)
# #
# # div(4,5)
# # div(2,4)
# # div(1,0)
#
# # def my_abs(x):
# #     if x >= 0:
# #         return x
# #     if x < 0:
# #         return -x
#
# # 定义方法查数据库
# # return 表示一个方法的结束，方法返回关键字
# # 方法定义
# # def math_cc():
# #     res = "平行四边形"
# #     return res
# #
# # # 方法调用
# # end = math_cc()
# # print(end)
# # ——————————————————————————————
# # 参数定义
# # 1.位置参数,调用时，参数有一个，传一个
# def s(a,b):
#     return a + b
# print(s(1,2))
#
# # 2.关键字参数 给参数设置默认值，如果调用时没有传参则用默认值，同时存在，位置参数在前面，关键字参数在后面
# def s(a,b=5):
#     return a+b
# print(s(1,2))
#
# # 调用传参
# # 按照位置传参
# print(s(88,99))
# # 按照关键字传参
# print(s(9999,b=1111))
# # 位置和关键字同时存在，位置在前，关键字在后
#
# # 动态参数定义
# #
# def cc(*args,**kwargs):
#     print(args)
#     # print(kwargs)
# cc(1,2,3,4,a=10,b=20,c=999999999999)

#
# def case1(a,b):
#     print(a)
#     print(b)
#     print('这是一条测试用例')
# case1(10,20,)
#
# def case2(a,b):
#     print(a)
#     print(b)
#     print('这是一条测试用例')
# case2(88,99,)



# def case(a,b):
#     print(a)
#     print(b)
#     print('这是一条测试用例')
# case(88,99,)
# def case_all(func,*args,**kwargs)
#     print("用例参数",args,kwargs)
#     r = func(*args,**kwargs)
#
#     print("用例结果",r)
# case_all(case,10,20)

'''
内置函数
'''
# a = 1000
# print(id(a)) # 获取变量内存地址

# i = input('请输入一个数据') # 获取控制台输入
# print(i)
#
# print(type("a")) # 获取变量类型
#
# print(isinstance(2,str)) # 判断变量类型
#
# l = [1,2,3,4]
# print(len(l)) # 获取变量值的个数 支持list tuple set dict str
#
# # 操作文件
# f = open("lacheln.txt","w") # 以写入的形式打开文件   a追加写入，b打开二进制文件
# f.write("hello!") # 写入数据
# f.close() #关闭文件
#
# f = open("b.txt",'r') # 以阅读的形式写入数据
# res = f.read() #写入数据
# print(res)
# f.close()