# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 下午5:25
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : python动态语言.py
# @Software: PyCharm

'''
动态语言的定义
动态编程语言是高级程序设计语言的一个类别，在计算机科学领域已被广泛应用。
它是一类在运行时可以改变其结构的语言：例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化。
动态语言目前非常具有活力。例如JavaScript便是一个动态语言，除此之外如PHP、Ruby、Python等也都属于动态语言，而C、C++等语言则不属于动态语言。----来自维基百科
'''

# 1.运行的过程中给对象绑定(添加)属性

class Person(object):
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age

p = Person(name='小明', age=20)
print(p.name)
print(p.age)

# 这里想给在运行过程的对象绑定属性 sex
p.sex = 'male'
print(p.sex)
print('-'*30)
# p.sex = 'male' 实际上就是动态给实例绑定属性，如果再实例一个Person对象，还是没有sex属性的，sex只限制于当前绑定的对象

# 2.运行的过程中给类绑定(添加)属性
p1 = Person('xiaozhang', 11)
print('姓名{name}, 年龄{age}'.format(
    name=p1.name,
    age=p1.age
))
# 给p1对象在运行时动态绑定对象
p1.sex = 'male'
p2 = Person('xiaowang', 19)
print('姓名{name}, 年龄{age}'.format(
    name=p2.name,
    age=p2.age
))

# 给Person类在运行时绑定属性sex，对所有Person实例有效
Person.sex = None
print(p2.sex) # 如果不写Person.sex = None 会报错AttributeError: 'Person' object has no attribute 'sex'

# 3.运行的过程中给类绑定(添加)方法
class Student(Person):
    def eat(self):
        print('eat food')

# 定义一个实例方法
def run(self, speed):
    print('%s在移动，速度是%d km/h' % (self.name, speed))

laowang = Student('老王', 28)
laowang.eat()
# p.run() # AttributeError: 'Person' object has no attribute 'run'
# 此时调用这个函数会报错，因为Student及其父类都没有run这个方法

# 运行过程中动态添加run方法
# 第一种方式：像添加属性那样添加，也是可以的，但是执行run时，该方法有个参数为self，我们需要把laowang本身传进去，而类本身的方法python解释器为我们自动添加了self为第一个参数
laowang.run = run
laowang.run(laowang, 122)

# 第二种方式：import types, 这种方式我们在执行run时不需要添加self参数
import types
xiaoliu = Student('xiaoliu', 12)
xiaoliu.run = types.MethodType(run, xiaoliu)
xiaoliu.run(301)

# 定义一个类方法
@classmethod
def testClass(cls):
    cls.num = 100

# 定义一个静态方法
@staticmethod
def testStatic():
    print('---test static---')

# 创建一个实例对象
xiaohan = Student('xiaohan', 18)
# 调用在class中的方法
xiaohan.eat()

# 给这个类添加实例方法
xiaohan.run = types.MethodType(run, xiaohan)
# 调用实例方法
xiaohan.run(1200)

# 给Student这个类绑定方法
Student.testClass = testClass
# 调用类方法
Student.testClass()
print('Student.num=%d'%Student.num)

# 给Student类绑定静态方法
Student.testStatic = testStatic
# 调用静态方法
Student.testStatic()
print('-'*30)

# 4.运行的过程中删除属性、方法
#del xiaohan.age
delattr(xiaohan, 'age')
print('-'*30)
'''
删除的方法:
1.del 对象.数属性名
2.delattr(对象, '属性名称')
通过以上的例子可以得到一个结论: 相对于动态语言，静态语言具有严谨性！所有请注意坑
那么怎么避免这种情况呢？请使用__slots__来约束一个类最多只能有有哪些属性
'''

# 5.__slots__
'''
动态语言与静态语言的不同
动态语言: 可以在运行的过程中，修改代码
静态语言: 编译时已经确定好代码，运行过程中不能修改
如果我们想要限制实例的属性怎么办？比如，只允许对Person实例添加name和age属性。只能限定实例对象的添加属性和方法
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
'''

class Product(object):
    __slots__ = ('name', 'price')

product = Product()
product.name = 'iPhone'
product.price = '200'
product.color = 'gray' # AttributeError: 'Product' object has no attribute 'color'
# __slots__的约束，Product不能添加__slots__以外的属性
# 注意: 使用__slots__定义的属性仅对当前类的所有实例有效，对于继续它的子类无效