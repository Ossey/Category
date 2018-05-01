# -*- coding: utf-8 -*-
# @Time    : 2018/4/30 上午10:35
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : 类作为装饰器.py
# @Software: PyCharm

# 实现__call__方法 ，python 中 类当作装饰器

class Test(object):
    def __init__(self, func):
        print('init')
        print('func name is %s' % func.__name__)
        # 使用__func 保存func引用，在__call__执行时调用
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('--装饰器中的功能--')
        self.__func()

@Test  # python解释器在执行到@Test时，会自动进行装饰，@Test相当于 Test(test) 创建一个Test实例，并传入参数test函数的引用
def test():
    print('--test--')

# 当@Test执行完成时，test=Test(test)，此时的test指向的并非test函数，而是执行Test的实例对象，
print(type(test))
# 当执行test()时，相当于执行了Test的实例对象，此时执行实例对象的__call__方法
test()