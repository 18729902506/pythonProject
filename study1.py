# print("hello world")

# 标识符
# 1、必须以字母或下划线开头，不能以数字开头
# 2、后面可以试试数字，字母，下划线
# 3、标识符大小写敏感
# 4、不可以使用关键字，又叫保留字

# name = 'zhangsan'
# print(name)

# 关键字
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from',
# 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# 导包
from keyword import kwlist
# 打印所有关键字
print(kwlist)
# 打印长度   33
print(len(kwlist))



# 注释
# 行注释
# 块注释：以三个单引号开始，以三个单引号结束。或者以三个双引号开始，以三个双引号结束
# '''
"""
print(1)
print(2)
print(3)
print(4)
"""
# '''

# python最具有特色的就是使用缩进来表示代码块，不需要使用大括号{}
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
# 缩进两种方式：使用tab或者空格，一个tab，默认四个空格，不应该缩进的地方，缩进了，运行就会报错。
# 编码规范，统一使用四个空格代表一个缩进
print(1)
print(2)
print(3)
print(4)

# 相同层次的代码要有相同的缩进
a, b = 1, 2
if a > b:
    print("a大于b")
else:
    print("a小于等于b")

# 多行语句    python通常是一行写完一条语句，但是如果语句很长，我们可以使用反斜杠(\)来实现多行语句
one, two, three = 1, 2, 3
total = one + two + three
print(total)

one, two, three = 1, 2, 3
total = one +\
        two +\
        three
print(total)


# 空行
# 函数之间或者类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始
# 空行与代码的缩进不同，空行并不是Python语法的一部分，书写时不插入空行，Python解释器运行也不会报错，但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构
# 空行也是程序代码的一部分

def method1():
    pass

def method2():
    pass

# print方法打印默认带空行，是换行的，如果不想带空行需要加end=''
print("冰美式")
print('热美式', end='')

# print打印多个对象时，默认使用一个空格间隔
print('冰美式', '热美式')

# print打印多个对象时，可以通过参数sep指定间隔符
print('冰美式', '热美式', sep='$')

# 导包的两种方式
# import 模块名(即py文件名称)            导入模块
# from 模块名 import 方法名             导入模块下的单个方法
# from 模块名 import 方法名1，方法名2     导入模块下的两个方法
# from 模块名 import *                 导入模块下的所有方法
# from 模块名 import 类名               导入模块下的类名

# sys.argv：模块.方法
import sys
print('=======python import mode======')
print('命令参数为：')
for i in sys.argv:
    print(i)
print('\n python路径为', sys.path)

# python也可以支持跨平台，可以运行在Mac上，可以运行在Linux系统上，运行在不同的系统上，可能需要一个加一个头（代码）
# 在windows下可以不写第一行注释
# !/usr/bin/env python     centos下，使用/usr/bin/env目录下的Python解释器运行脚本
# coding:utf-8             windows下，指定文件编码格式
# -*- coding:utf-8 -*-     windows下，推荐，因为支持的编辑器更多

# help函数
# 调用Python的help函数可以打印输出一个函数的文档字符串
# 例如 help(max)，可以查看max内置函数的参数列表和规范的文档

help(max(2, 4, 1))




















