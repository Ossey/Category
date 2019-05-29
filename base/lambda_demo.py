#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 10:07 AM
# @Author  : xiaoyuan
# @Site    : https://github.com/tuxi
# @File    : lambda_demo.py
# @Software: PyCharm

'''
lambda只是一个表达式，函数体比def简单很多，很多时候定义def，然后写一个函数太麻烦，这时候就可以用lambda定义一个匿名函数。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
'''

# lambda表达式是起到一个函数速写的作用。允许在代码内嵌入一个函数的定义。
# 如上所示，使用lambda表达式定义了一个匿名函数，用于筛选100以内的3的倍数，并生成一个列表。
from functools import reduce

l = list(filter(lambda x:True if x % 3 == 0 else False, range(100)))
print(l)

def make_repeat(n):
    '''
    :param n:
    :return: lambda 表达式
    '''
    return lambda s : s * n
# 然后，要使用的时候可以用一个变量来接收，显示double变量，double变量是一个函数，并且需要一个参数，参见lambda表达式，需要一个s参数。
d = make_repeat(10)
print(d(100))

# zip()：字面意思理解，就是zip打包，可以将多个序列进行打包，它会将序列拆分，然后把第一个序列和第二个序列的元素依次组成元组，2个一组组合成列表。
# 不过要注意的是，这是以最短序列来组合的，就是说如果一个序列比较长，一个比较短的话，组合只会进行到断序列的最后一个元素，多余的部分会被抛弃。
z = zip("str", "syr1")
print(list(z))

# 将lambda函数作为参数传递给其他函数。

# map()：映射，用法和filter()类似，也是将序列放入函数进行运算，但是，不论运算结果为什么，
# map() 都将忠实反馈，这是map()和filter()的主要区别。请注意，filter()和map()中的function都必要有一个返回值。
ret = list(map(lambda x: True if x % 3 == 0 else False, range(100)))
print(ret)

# filter函数。此时lambda函数用于指定过滤列表元素的条件。例如filter(lambda x: x % 3 == 0, [1, 2, 3])指定将列表[1,2,3]中能够被3整除的元素过滤出来，
# 其结果是[3]。
it = filter(lambda x: x % 3 == 0, [1, 2, 3])
for item in it:
    print(item)

# sorted函数。
# 此时lambda函数用于指定对列表中所有元素进行排序的准则。
# 例如sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]按照元素与5距离从小到大进行排序，
# 其结果是[5, 4, 6, 3, 7, 2, 8, 1, 9]。
it1 = sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))
for item in it1:
    print(item)

# map函数。
# 此时lambda函数用于指定对列表中每一个元素的共同操作。例如map(lambda x: x+1, [1, 2,3])将列表[1, 2, 3]中的元素分别加1，
# 其结果[2, 3, 4]。
print(10*"-")
it2 = map(lambda x: x+1, [1, 2, 3])
for item in it2:
    print(item)
print(10*"-")

# reduce函数。
# 此时lambda函数用于指定列表中两两相邻元素的结合条件。
# 例如reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])将列表 [1, 2, 3, 4, 5, 6, 7, 8, 9]中的元素从左往右两两以逗号分隔的字符的形式依次结合起来，
# 其结果是'1, 2, 3, 4, 5, 6, 7, 8, 9'。
str1 = reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(str1)



