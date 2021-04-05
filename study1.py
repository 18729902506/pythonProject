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




































