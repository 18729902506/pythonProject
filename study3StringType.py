# 字符串
# <class 'str'> <class 'str'>
# 1969756754928 1969756754928
str1 = 'xiao zhang'
str2 = "xiao zhang"
print(type(str1), type(str2))
print(id(str1), id(str2))

'''
    字符串的定义有两种，一种是单引号，一种是双引号，表示的是一样的
    Python中的字符串用单引号或者双引号括起来，同时使用反斜杠(\)转义特殊字符
    字符串的截取的语法格式如下：
    变量[头下标:尾下标]
    索引值以0为开始值，-1为从末尾的开始位置
    加号(+)是字符串的连接符，星号(*)表示复制当前字符串，紧跟的数字为复制的次数
'''

'''
    切片
    字符串是有序，有下标的，每一位可以通过下标来表示，从左到右，第一位是0位，最后一位的下标是总长度-1
    中括号中的第一位表示起始的位置下标，第二位表示截止位置下标，左闭右开
    print(str3[0:4])   zhan
    print(str3[1:4])   han
'''

'''
    反斜杠(\)可以作为续行符，表示下一行是上一行的延续
    注意：
        Python没有单独的字符类型，一个字符就是长度为1的字符串
        反斜杠可以用来转义，使用r可以让反斜杠不发生转义
        字符串可以用+运算符连接在一起，用*运算符重复
        Python中发字符串有两种索引方式，从左到右以0开始，从右往左以-1开始
        Python中的字符串不能改变
'''
str3 = 'zhang san'

# 左闭右开 zhan
# print(str3[0:4])
# print(str3[1:4])

# zhang san  下面的方法都表示取整个字符串的长度
# print(str3)
# print(str3[0:len(str3)])
# print(str3[:])
# print(str3[0:])
# print(str3[0:9])

# zhang sa   -1代表最后一位字符的下标，也就是倒数第一位，因为左闭右开，所以结果不包含最后一位 n
# print(str3[0:-1])

# 步长   第三位数字代表步长，可以让切片结果跳着取，2代表隔一位取一个，3代表隔两位取一个
# print(str3[0:9])
# print(str3[0:9:2])   # zagsn
# print(str3[0:9:3])   #zns


# 转义符 \n代表回车，相当于换行
# 常见的转义字符：\n代表回车，   \r代表换行    \t代表制表符    \\代表一个反斜杠
# str1 = 'zhangsan'
# print(str1)

# str1 = 'zhang\nsan'
# zhang
# san
# print(str1)

# zhang\nsan  字符串前面加一个r或者R，表示字符串原样输出，即里面的转义符不转义
# str1 = r'zhang\nsan'
# print(str1)

str1 = "千锋"
str2 = "教育"
str3 = str1 + str2  # 两个string类型的对象可以使用+，拼接在一起
# 千锋教育
print(str3)

a,b = 1,2
print(a+b) # 3 如果加号两边是数值型，会做算数运算
# print(str1 + a) # 字符串和数值型不能使用+拼接，会报错

str1 = "千峰"
print(str1 * 2) # 千峰千峰，重复显示字符串str1的内容为2次


# 两次的内存地址空间不一样    Python中的字符串不能改变。   不可变的对象修改了之后，，内存地址会变。对于可变的对象，修改了之后，内存地址不会变
# 2024644653720
# 2024644653632
str1 = "千峰"
print(id(str1))
str1 = "教育"
print(id(str1))


# [1, 2]
# 1600080761736
# [1, 2, 3]
# 1600080761736
list1 = [1,2]
print(list1)
print(id(list1))
list1.append(3)
print(list1)
print(id(list1))

# 字符串常用的内置方法
str1 = 'zhangsan'
print(str1.isdigit()) # false 用来判断字符串是否为纯数字，是，返回true，否则，返回false
print(str1.isupper()) # false，字符串是否为纯大写
print(str1.islower()) # true，字符串是否为纯小写
print(str1.isalpha()) # true，字符串是否为纯字母
print(str1.isalnum()) # true 是否是纯字母，纯数字，或者字母加数字
print(str1.index("a")) # 2 返回字母a第一次出现位置的下标
print(str1.index("an")) # 2  an是一个整体
print(str1.replace('a','u')) # zhungsun 将之前的字符串的a，都变成u
print(str1.replace('a','u',1)) # zhungsan 将之前的字符串的a，只替换一次


# 将一个列表转成字符串  123
list1 = ['1', '2', '3']
print(''.join(list1))
print('#'.join(list1))  # 1#2#3

# ['zh', 'ngs', 'n']
# ['zh', 'ngsan']
print(str1.split('a')) # 将指定的字符串使用指定的字符分隔
print(str1.split('a', 1)) # 将指定的字符串使用指定的字符分隔,分隔一次，以列表的形式返回















