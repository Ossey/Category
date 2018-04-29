# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 下午9:29
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : 装饰器.py
# @Software: PyCharm

# 1.python中同一模块下函数重名
# 注意：当函数重名时，python解释器在执行时会执行最后定义的那个函数，而前面定义的都不会被执行, 这是因为函数变量指向了最后的那个函数，所以执行的也是最后的函数
# 示例
#def test():
#    print('test')
#def test():
#    print('test1')
#test()

print('-'*30)

# 2.装饰器的基本实现
def test(func):
    def inner():
        print('正在验证权限')
        func()
    return inner


@test # @test等价于 innerFunc = test(f1) 把f1函数的引用作为参数传入到test函数中，当执行f1时会先执行test1()
def f1():
    print('f1权限验证完成')

# 执行test函数时，把fi函数的引用作为参数传入进去了, test函数的返回值为inner()函数的引用
# f1接收了inner函数的引用
f1 = test(f1)
# 执行f1就等于执行inner函数，而inner函数内部执行了test函数的参数f1
f1()
# 以上就是装饰器实现的最基本原理

@test
def f2():
    print('f2权限验证完成')

f2()
print('-'*30)
# 3.多个装饰器示例

# 定义函数: 完成包裹数据
def makeBold(fn):
    def warpped():
        print('---1---')
        return "<b>" + fn() + "</b>"
    return warpped

# 定义函数: 完成包裹数据
def makeItalic(fn):
    def warpped():
        print('---2---')
        return "<li>" + fn() + "</li>"
    return warpped

@makeBold   # 等同于 test1 = makeBold(test1) , 当执行此句代码时，test1指向了makeBold中的warpped函数
@makeItalic # 等同于 test1 = makeItalic(test1), 当执行此句代码时，test1指向了makeItalic中的warpped函数
def test1():
    print('---3---')
    return 'hello word'

ret = test1()
print(ret)
# 理解起来有点抽象：多个装饰器，装饰时倒着装，执行时从上往下执行
'''
执行结果:
---1---
---2---
---3---
<b><li>hello word</li></b>
'''
print('-'*30)
# 4.装饰器执行的时间
def w1(fn):
    print("---正在装饰---")
    def inner():
        print("---正在验证权限---")
        fn()
    return inner

# python解释权在执行到@w1时，就等于执行了f2 = w1(f2)，那么就会自动进行装饰，而不是等到调用的时候才执行
@w1 # 等同于 f2 = w1(f2)
def f2():
    print('---f2---')

f2() # 在执行f2时已经执行了w1函数，也就是已经进行装饰了
print('-'*30)
# 5.装饰器对无参数的函数进行装饰
def func(funcName):
    print('func--1--')
    def func_in():
        print('func_in--1--')
        funcName()
        print('func_in--2--')
    print('func--2--')
    return func_in

@func # 等同于 f3 = func(f3)
def f3():
    print('--f3--')
# f3 = func(f3)
f3()
print('-'*30)

# 6.装饰器对有参数的函数进行装饰
def func6(func_name):
    print('func6--1--')
    def func_in(a, b):
        print('func_in6--1--')
        func_name(a, b)
        print('funcin_6--2--')
    print('func6--2--')
    return func_in

@func6  # 等同于test6 = func6(test6)，此时test6指向了func6中的func_in函数
def test6(a, b):
    print('---test6-a=%d, b=%d--' %(a, b))

test6(10, 20) # 当执行test6时，也就等于执行了内部函数func_in()，也就是说func_in的参数必须与test6的参数相同，而且执行func_name()也必须传入相同的参数，不然报错参数问题
print('-'*30)

# 7.装饰器对不定长参数的函数进行装饰
def func7(func_name):
    print('func7--1--')
    def func_in(*args, **kwargs):
        print('func_in7--1--')
        # 注意:*args, **kwargs用于不定长参数，函数参数为这两个时，传递时也要原封不动(也就是*args，不要写成args)的传递出去，不然其他函数接受时无法拆包会crash，*args是元组，**kwargs是字典
        func_name(*args, **kwargs)
        print('func_in7--2--')
    print('func7--2--')
    return func_in

def test7(a, b, c):
    print('---test7---a=%d, b=%d, c=%d' %(a, b, c))
test7(10, 20, 30)
# def test7(a, b, c, d):
#     print('---test7---a=%d, b=%d, c=%d, d=%d' %(a, b, c, d))
# test(10, 20, 30, 40)
print('-'*30)

# 装饰器对有返回值的函数进行装饰
def func8(func_name):
    print('func8--1--')
    def func_in():
        print('func_in--1--')
        ret = func_name()  # 保存返回值
        print('func_in--2--')
        return ret  # 返回返回值
    print('func8--2--')
    return func_in

@func8
def test_return():
    print('test_retun')
    return 'return value haha'
ret = test_return()
print(ret)

# 9.通用型装饰器(对有无返回值和有无参数均使用)
def gloabl(func_name):
    print('global--1--')
    def func_in(*args, **kwargs):
        print('func_in--1--')
        ret = func_name(*args, **kwargs)
        print('func_in--2--')
        return ret
    print('global--2--')
    return func_in

@gloabl
def test_global(a, b):
    return a * b

ret = test_global(10, 20)
print(ret)
print('-'*30)

# 10.装饰器带参数
def func_arg(arg):
    def func(funcName):
        def func_in():
            print('记录日志--%s--')
            # 当装饰器参数是 哈哈哈是执行两次，是呵呵时执行一次
            if arg == '哈哈哈':
                funcName()
                funcName()
            elif arg == '呵呵':
                funcName()
        return func_in
    return func

# @func_arg带参数的装饰器，
# 当python解释器执行到@func_arg(arg='哈哈哈')时，实际上执行了func_arg()函数，而func_arg函数返回值是func函数，那么此时装饰器则为func(funcName)
@func_arg(arg='哈哈哈')
def test_arg():
    print('--test--')

test_arg()

# 带参数的装饰器作用:
'''
当选择对什么样的东西选择什么装饰器时有用，
同一个装饰器，传的参数不一样，那么就可以做不同的事情，也就是根据参数判断
'''

