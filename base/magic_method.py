# -*- coding: utf-8 -*-
# @Time    : 2016/6/12 下午11:37
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : magic_method.py
# @Software: PyCharm

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

company = Company(['tom', 'jay', 'sey'])

for em in company:
    print(em)