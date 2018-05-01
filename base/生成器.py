# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 下午7:50
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : 生成器.py
# @Software: PyCharm

# python生成器generator
'''
从字面上来看，生成器应该是用来生成数据的
'''

# 1.生成器的作用
'''
按照某种算法不断生成新的数据，直到满足某一个指定的条件约束
'''

# 2.生成器的构造方式
'''
构造生成器的两种方式:
1.使用类似列表生成式的方式生成，列表生成时使用的是[]，而生成器使用()，比如(2*n + 1 for n in range(3, 11)), 返回的不再是列表，而是一个生成器
2.使用包含yield的函数生成
注意：如果计算比较简单，可以直接把列表生成式改成generator；但是，日光计算过程比较复杂，就只能通过包含yield的函数来构造generator；
并且在python 3，3之前的版本中，不允许迭代函数中包含return的语句
'''

# 生成器构造示例
# 示例1：
# 使用类似列表生成时的方式构造生成器
g1 = (2*2 + 1 for n in range(3, 6))
# 使用包含yield的函数构造生成器
def my_range(start, end):
    for n in range(start, end):
        yield  2*n + 1

g2 = my_range(3, 6)
print(type(g1))
print(type(g2))
print('-'*30)

# 示例2：构造裴波那契数列的生成器
from base.test_generator import *

a = cteateNum()
print(a)
# print(a.__next__())
# # print(next(a)) 等同于 print(a.__next__())
#
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
print('-'*30)

# 生成器执行的过程与特征
'''
生成器执行过程：
在执行过程中，遇到yield关键字就会中断执行，下次调用则继续从上次中断的位置继续执行
'''
'''
生成器执行的特征：
1.只有在调用时才会生成相应的数据
2.只记录当前的位置
3.只能next，不能prev
'''

# 生成器的调用方式
'''
要调用生成器产生新的元素，有两种方式：
1.调用内置的next(生成器对象)方法，或者 生成器对象.__next__()
2.使用循环对生成器对象进行遍历(推荐)
3.调用生成器对象的send()方法
'''
# 使用next()方法遍历生成器时，最后是以抛出一个StopIeration异常终止。
# 使用循环遍历生成器时比较简洁，且最后不会抛出一个StopIeration异常。因此使用循环的方式遍历生成器的方式才是被推荐的。
# 需要说明的是：如果生成器函数有返回值，要获取该返回值的话，只能通过在一个while循环中不断的next()，最后通过捕获StopIteration异常

# 示例3：使用循环遍历生成器
for x in g1:
    print(x)
for x in g2:
    print(x)
print('-'*30)

# 示例4：调用生成器对象的send()方法
def my_range1(start, end):
    for n in range(start, end):
        ret = yield 2*n + 1
        print(ret)
g3 = my_range1(8, 20)
# g3.__next__()
# 注意第一次send时必须先执行__next__()或者send(None)，不然抛出异常 TypeError: can't send non-None value to a just-started generator
g3.send(None)
g3.send('hello01')
g3.send('heool02')
print('-'*30)

# 生成器和列表生成式对比
'''
既然通过列表生成式就可以直接创建一个新的list，那么为什么还要有生成器存在呢？
因为列表生成式是直接创建一个新的list，它会一次性的把所有数据都放到内存中，这回存在以下几个问题：
1.内存容量有限，因此列表容量是有限的；
2.当列表的数据很大时，会占有大量的内存空间，如果我们仅仅需要访问前面有限个元素时，就会造成内存资源的极大浪费；
3.当数据量很大时，列表生成式的返回时间会很慢；
'''
'''
而生产器中的元素是按照指定的算法推算出来的，只有调用时才会生成相应的数据，这样就不必一次性的把所有的数据生成，从而节省了大量的内存空间，
这使得其生成的元素个数几乎是没有限制的，并且操作的返回时间也是非常快速的（仅仅是创建一个变量而已）
'''

# 示例：对比一下生成一个10000万个数字的列表，分别看下用列表生成式和生成器时返回结果的时间和所占的内存空间大小：
import time
import sys

# 列表生成式
time_start = time.time()
m1 = [x for x in range(10000000)]
time_end = time.time()
print('列表生成式返回结果花费的时间: %s' % (time_end - time_start))
print('列表生成式返回结果占用内存大小 %s' % sys.getsizeof(m1))

# 生成器
def my_range_m(start, end):
    for x in range(start, end):
        yield x
time_start = time.time()
m2 = my_range_m(0, 10000000)
time_end = time.time()
print('生产器返回结果花费的时间：%s' % (time_end - time_start))
print('生成器返回结果占用内存大小 %s' % sys.getsizeof(m1))
