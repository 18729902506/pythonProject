# 字符串
# <class 'str'> <class 'str'>
# 1969756754928 1969756754928
str1 = 'xiao zhang'
str2 = "xiao zhang"
print(type(str1), type(str2))
print(id(str1), id(str2))

'''
    字符串的定义有两种，一种是单引号，一种是双引号，表示的是一样的
'''

'''
    切片
    字符串是有序，有下标的，每一位可以通过下标来表示，从左到右，第一位是0位，最后一位的下标是总长度-1
    中括号中的第一位表示起始的位置下标，第二位表示截止位置下标，左闭右开
    print(str3[0:4])   zhan
    print(str3[1:4])   han
'''
str3 = 'zhang san'

# 左闭右开 zhan
print(str3[0:4])
print(str3[1:4])

# zhang san  下面的方法都表示取整个字符串的长度
print(str3)
print(str3[0:len(str3)])
print(str3[:])
print(str3[0:])
print(str3[0:9])

# zhang sa   -1代表最后一位字符的下标，也就是倒数第一位，因为左闭右开，所以结果不包含最后一位 n
print(str3[0:-1])

# 步长   第三位数字代表步长，可以让切片结果跳着取，2代表隔一位取一个，3代表隔两位取一个
print(str3[0:9])
print(str3[0:9:2])   # zagsn
print(str3[0:9:3])   #zns






























