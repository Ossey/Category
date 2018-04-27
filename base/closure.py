# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 下午10:07
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : closure.py
# @Software: PyCharm

# 闭包

def test(num):
    print('----1----')
    def test_in(num1):
        print('----2----')
        print(num + num1)
        print('----3----')
    return test_in

# 使用t变量接受返回的函数
t = test(100)
# 执行内部函数
t(2)
t(200)