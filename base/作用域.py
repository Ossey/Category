# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 下午1:34
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : 作用域.py
# @Software: PyCharm

# python 作用域

# LEGB原则：
'''
python中作用域有四种:
L (local)局部作用域
E (Enclosing) 闭包函数外的函数中的
G (Global) 全局作用域
B (Built-in) 内建作用域
'''

# python 按照 LEGB原则搜索变量，即优先级L>E>G>B

dir = 1 # Global

def outer():
    dir = 2 # Enclosing
    def inner():
        dir = 3 # Local
        return dir
    # 打印函数内的所有局部变量
    print(locals())
    return inner


outer = outer()

# 打印当前模块中的所有全局变量
print(globals())

print(outer())

# Python两个内置函数——locals 和globals
'''
这两个函数主要提供，基于字典的访问局部和全局变量的方式。
在理解这两个函数时，首先来理解一下python中的名字空间概念。Python使用叫做名字空间的
东西来记录变量的轨迹。名字空间只是一个字典，它的键字就是变量名，字典的值就是那些变
量的值。实际上，名字空间可以象Python的字典一样进行访问


每个函数都有着自已的名字空间，叫做局部名字空间，它记录了函数的变量，包括函数的参数
和局部定义的变量。每个模块拥有它自已的名字空间，叫做全局名字空间，它记录了模块的变
量，包括函数、类、其它导入的模块、模块级的变量和常量。还有就是内置名字空间，任何模
块均可访问它，它存放着内置的函数和异常。


当一行代码要使用变量 x 的值时，Python会到所有可用的名字空间去查找变量，按照如下顺序：


1.局部名字空间 - 特指当前函数或类的方法。如果函数定义了一个局部变量 x，Python将使用
  这个变量，然后停止搜索。
2.全局名字空间 - 特指当前的模块。如果模块定义了一个名为 x 的变量，函数或类，Python
  将使用这个变量然后停止搜索。
3.内置名字空间 - 对每个模块都是全局的。作为最后的尝试，Python将假设 x 是内置函数或变量。


如果Python在这些名字空间找不到 x，它将放弃查找并引发一个 NameError 的异常，同时传递
There is no variable named 'x' 这样一条信息。
'''

# 局部变量函数locals例子(locals赶回一个名字/值对的字典)：
def foo(arg, a):
    x = 1
    y = 'xxxx'
    for i in range(10):
        j = 1
        k = 1
    print(locals())

# 调用函数(函数内会打印locals())
foo(1, 2)
# 打印结果: {'k': 1, 'j': 1, 'i': 9, 'y': 'xxxx', 'x': 1, 'a': 2, 'arg': 1}

'''
from module import 和 import module之间的不同。使用 import module，模块自身被导入，
但是它保持着自已的名字空间，这就是为什么你需要使用模块名来访问它的函数或属性（module.function）
的原因。但是使用 from module import，实际上是从另一个模块中将指定的函数和属性导入到你自己的名字
空间，这就是为什么你可以直接访问它们却不需要引用它们所来源的模块的原因。
'''



