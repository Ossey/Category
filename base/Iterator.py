# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 下午10:43
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : Iterator.py
# @Software: PyCharm

from collections import Iterable, Iterator

# Python中 list，truple，str，dict这些都可以被迭代，但他们并不是迭代器。为什么？
# 因为和迭代器相比有一个很大的不同，list/truple/map/dict这些数据的大小是确定的，也就是说有多少事可知的。
# 但迭代器不是，迭代器不知道要执行多少次，所以可以理解为不知道有多少个元素，每调用一次next()，就会往下走一步，是惰性的。

# 判断是不是可以迭代，用Iterable
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance('', Iterable))
print(isinstance({}, Iterable))
print(isinstance(100, Iterable))
# 上述除了100，都是可迭代的

# 判断是不是迭代器，用Iterator
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance((x for x in range(10)), Iterator)) # 生成器
# 上述除了生成器，都是迭代器

a = (x for x in range(10))
#print(a.next())
# 生成器执行next() 函数抛出异常：
# Traceback (most recent call last):
#  File "/Users/swae/Documents/Github/LearnPython/base/Iterator.py", line 29, in <module>
#    print(a.next())
# AttributeError: 'generator' object has no attribute 'next'
# 原因是在python 3.x中 generator（有yield关键字的函数则会被识别为generator函数）中的next变为__next__了,next是python 3.x以前版本中的方法

# 正确：
print(a.__next__())
print(a.__next__())
print(a.__next__())


'''
所以，
凡是可以for循环的，都是Iterable

凡是可以next()的，都是Iterator

集合数据类型如list，truple，dict，str，都是Itrable不是Iterator，但可以通过iter()函数获得一个Iterator对象

Python中的for循环就是通过next实现的
'''

for x in [1, 2, 3, 4, 5]:
    pass

# 等价于
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        # 获取下一个值
        x = next(it)
        print(x)
    except StopIteration as e:
        # 遇到StopIteration异常就退出循环
        print(str(e))
        break
