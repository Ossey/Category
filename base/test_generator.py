# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 下午8:23
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : test_generator.py
# @Software: PyCharm

# 裴波那契数列

def cteateNum():
    print('---start---')
    a,b = 0,1
    for n in range(5):
        print('---1---')
        yield b
        print('---2---')
        a,b = b, a+b
        print('---3---')
    print('---stop---')