# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 下午10:14
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : property.py
# @Software: PyCharm

# 第一种property
class Test(object):
    def __init__(self):
        # 定义私有属性__num
        self.__num = 100

    def setNum(self, num):
        if isinstance(num, int):
            self.__num = num

    def getNum(self):
        return self.__num

    num = property(getNum, setNum)

t = Test()
t.setNum(50)
print(t.getNum())
print('-'*50)
t.num = 200
print(t.num)

# 第一种property 通过装饰器
class Test1(object):
    def __init__(self):
        self.__num = 100

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        if isinstance(num, int):
            self.__num = num

t1 = Test1()
t1.num = 1000
print('-'*50)
print(t1.num)
