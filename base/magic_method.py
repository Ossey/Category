# -*- coding: utf-8 -*-
# @Time    : 2016/6/12 下午11:37
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : magic_method.py
# @Software: PyCharm

'''
Python的魔法方法 .
基本行为和属性
__init__(self[,....])构造函数 . 在实例化对象的时候会自动运行
__del__(self)析构函数 . 在对象被回收机制回收的时候会被调用
__str__(self)输出函数 . 在实例对象请求输出的时候会被调用.
__repr__(self). 当直接调用实例对象的时候会被调用
__new__(cls,[,...]). 她的第一个参数是这个类 , 其他的参数被直接传送到 __init__ . 并且__new__是一个对象实例化的时候所调用的第一个方法(所以可以在这里做点手脚) ,
__bool__(self)  定义当被bool类 调用的时候 应当返回的值
__len__(self) 定义单被len调用的时候的行为.
__hash__(self) 定义当被hash 调用的时候返回的函数 .
__getattr__ (self,name)定义当用户师徒访问一个不存在的属性时 所执行的行为 .
__getattribute__(self,name)定义当该属性被访问时的行为
__setattribute__ (self,name,value)定义一个属性被设置时的行为 .
__delattr__(self,name)定义一个属性被删除时的行为
__dir__(self) 定义dir被调用时的行为.
__get__(self,instance,owner) 定义当描述符 被取得时的行为
__set__(self,instance,owner)定义当描述符的值被改变是的行为.
__delete__(self,instance) 定义当描述符被删除时的行为
比较操作符,算术运算符,反运算,增量运算,一元操作,类型转换,上下文管理,容器类型.
当属性的名称和方法的名称一样的时候 , 属性的名称会自动覆盖方法的名称  , 所以属性和方法的名称影噶尽量分开 .
'''

import time as t
import sys

# 示例1
# 通过__getitem__魔法函数，将Company类构建为一个迭代器
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

company = Company(['tom', 'jay', 'sey'])

for em in company:
    print(em)

# 示例2
class MyTimer(object):
    def __init__(self):
        # 先设置各种属性，防止使用不当错
        self.unit = ['年', '月', '日', '小时', '分钟', '秒']
        self.prompt = '未开始计时'
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        print("我被调用了:" + str(type(self)))
        return self.prompt

    __repr__ = __str__

    def start(self):
        self.begin = t.localtime()
        print("计时开始")

    def stop(self):
        if not self.begin:
            print("请先开始调用 start")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束")

    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]

t1 = MyTimer()
t1.stop()
t1.start()
t1.stop()
print(t1)
