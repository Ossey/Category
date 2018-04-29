# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 下午6:50
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : 列表生成式.py
# @Software: PyCharm


# 列表生成式
'''
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
'''

# 基础语法格式
# [exp for iter_var in iterable]
'''
工作过程：

迭代iterable中的每个元素；
每次迭代都先把结果赋值给iter_var，然后通过exp得到一个新的计算值；
最后把所有通过exp得到的计算值以一个新列表的形式返回。
'''


'''
相当于这样的过程：
L = []
for iter_var in iterable:
    L.append(exp)
'''

'''
带过滤功能语法格式:
[exp for iter_var in iterable if_exp]

'''
'''
工作过程：

迭代iterable中的每个元素，每次迭代都先判断if_exp表达式结果为真，如果为真则进行下一步，如果为假则进行下一次迭代；
把迭代结果赋值给iter_var，然后通过exp得到一个新的计算值；
最后把所有通过exp得到的计算值以一个新列表的形式返回。
'''

'''
相当于这样的过程：

L = []
for iter_var in iterable:
    if_exp:
        L.append(exp)
'''

'''
循环嵌套语法格式

[exp for iter_var_A in iterable_A for iter_var_B in iterable_B]
'''
'''
工作过程：
每迭代iterable_A中的一个元素，就把ierable_B中的所有元素都迭代一遍。

相当于这样的过程：

L = []
for iter_var_A in iterable_A:
    for iter_var_B in iterable_B:
        L.append(exp)
'''

#列表生成式的应用场景
'''
其实列表生成式也是Python中的一种“语法糖”，也就是说列表生成式应该是Python提供的一种生成列表的简洁形式，应用列表生成式可以快速生成一个新的list。
它最主要的应用场景是：根据已存在的可迭代对象推导出一个新的list。
'''

# 示例
# 我们可以对几个生成列表的要求分别通过“不使用列表生成式”和“使用列表生成式”来实现，然后做个对比总结。

# 示例1： 生成一个从3到10的数字列表

# 第一种方式：不使用列表生成式实现
list1 = list(range(3, 11))
print(list1)
# 第二种方式：使用列表生成式实现
list2 = [x for x in range(3, 11)]
print(list2)
# 上面两种方式结果相同

# 示例2：生成一个2n+1的数字列表，n为从3到11的数字
# 第一种方式：不使用列表生成式实现
list3 = []
for n in range(3, 11):
    list3.append(2*n + 1)

print(list3)
# 第二种方式：使用生成式实现
list4 = [2 * n + 1 for n in range(3, 11)]
print(list4)
# 上面两种方式结果相同

# 示例3：过滤出一个指定的数字列表中值大于20的元素
l =  [3, 7, 11, 14, 19, 33, 26, 57, 99]

# 第一种方式：不是呀列表生成时实现
list5 = []
for n in l:
    if n > 20:
        list5.append(n)
print(list5)
# 使用列表生成时实现
list6 = [x for x in l if x > 20]
print(list6)

# 示例4：计算两个集合的全排列，并将结果保存到一个新的列表中
l1 = ['香蕉', '苹果', '橙子']
l2 = ['可乐', '牛奶']
# 不使用列表生成式实现
list7 = []
for x in l1:
    for y in l2:
        list7.append((x, y))
print(list7)
# 使用列表生成式实现
list8 = [(x, y) for x in l1 for y in l2]
print(list8)

# 示例5：将一个字典转换成由一组元组组成的列表，元组的格式为(key, value)
dic = {'tom': 15, 'jay': 20, 'peter': 13}
# 不使用列表生成式实现
list9 = []
for k, v in dic.items():
    list9.append((k, v))
print(list9)
# 使用列表生成式实现
list10 = [(k,v) for k, v in dic.items()]
print(list10)

# 列表生成式与map()、filter()等高阶函数功能对比
# 示例1：把一个列表中所有的字符串转换成小写，非字符串元素原样保留
l = ['TOM', 'PETTER', 10, 'Jerry']
# 列表生成式实现
list11 = [x.lower() if isinstance(x, str) else x for x in l]
print(list11)
# 用map()函数实现
list12 = list(map(lambda x: x.lower() if isinstance(x, str) else x, l))
print(list12)

# 示例2：把一个列表中所有的字符串转换成小写，非字符串元素移除
# 用列表生成式实现
list13 = [x.lower() for x in l if isinstance(x, str)]
print(list13)
# 用map()和filter()实现
list14 = list(map(lambda x: x.lower(), filter(lambda  x: isinstance(x, str), l)))
print(list14)

'''
对于大部分需求来讲，使用列表生成式和使用高阶函数都能实现。
但是map()和filter()等一些高阶函数在Python3中的返回值类型变成了Iteraotr（迭代器）对象（在Python2中的返回值类型为list），
这对于那些元素数量很大或无限的可迭代对象来说显然是更合适的，因为可以避免不必要的内存空间浪费。
'''