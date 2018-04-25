# -*- coding: utf-8 -*-
# @Time    : 2016/6/12 下午11:37
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : magic_method.py
# @Software: PyCharm

'''
魔法方法就是可以给你的类增加魔力的特殊方法，如果你的对象实现（重载）了这些方法中的某一个，那么这个方法就会在特殊的情况下被 Python 所调用，你可以定义自己想要的行为，而这一切都是自动发生的。它们经常是两个下划线包围来命名的（比如 __init__，__lt__），Python的魔法方法是非常强大的，所以了解其使用方法也变得尤为重要！

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


# __init__(self[, ...])，__new__(cls[, ...])，__del__(self)
'''
__init__ 构造器，当一个实例被创建的时候初始化的方法。但是它并不是实例化调用的第一个方法，__new__才是实例化对象调用的第一个方法，它只取下 cls参数，并把其他参数传给 __init__。 __new__很少使用，但是也有它适合的场景，尤其是当类继承自一个像元组或者字符串这样不经常改变的类型的时候。

　　__new__ 使用时注意以下四点：
1. __new__ 是在一个对象实例化的时候所调用的第一个方法
2. 它的第一个参数是这个类，其他的参数是用来直接传递给 __init__ 方法
3. __new__ 决定是否要使用该 __init__ 方法，因为 __new__ 可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例，如果 __new__ 没有返回实例对象，则 __init__ 不会被调用
4. __new__ 主要是用于继承一个不可变的类型比如一个 tuple 或者 string
5. __new__ return的是一个构建的实例
'''

# 实例 __new__ 实现单例模式
class Persion(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Persion, cls).__new__(cls)
        return cls.instance

a = Persion('p1', 20)
b = Persion('p2', 21)
print(id(a))
print(id(b))
# 通过打印可以看出a和b内存地址是相同的，是同一个实例对象
#单例作用：
#第一、控制资源的使用，通过线程同步来控制资源的并发访问；
#第二、控制实例产生的数量，达到节约资源的目的。
#第三、作为通信媒介使用，也就是数据共享，它可以在不建立直接关联的条件下，让多个不相关的两个线程或者进程之间实现通信。
#比如，数据库连接池的设计一般采用单例模式，数据库连接是一种数据库资源。
#__del__ 析构器，当实例被销毁时调用

# 实例__call__(self[,args ...])，__getitem__(self,key)，__setitem__(self,key,value)

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.instance = add

    def __call__(self, *args, **kwargs):
        return self.instance(*args)

def add(args):
    return args[0] + args[1]

a = Student('s1', 20)
print(a([1, 2]))
#这里将打印 3
#可见当创建a这个对象之后，如果定义了__call__函数则对象是可以像函数一样调用的

# 通过__getitem__魔法函数，将Company类构建为一个迭代器
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

company = Company(['tom', 'jay', 'sey'])

for em in company:
    print(em)
#这里打印的是 'tom' 'jay' 'sey'
#可见__getitem__使实例可以像列表一样访问

#__getitem__ 定义获取容器中指定元素的行为，相当于self[key]
class Person1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._registry = {
            'name': name,
            'age': age
        }
        self.instance = add

    def __call__(self, *args, **kwargs):
        return self.instance(*args)

    def __getitem__(self, key):
        if key not in self._registry.keys():
            raise Exception('Please registry the key: %s first', key)
        return self._registry[key]

    def __setitem__(self, key, value):
        if key not in self._registry.keys():
            raise Exception('Please registry the key: %s first', key)
        self._registry[key] = value

a = Person1('p1', 20)
print(a['name'], a['age'])
a['name'] = 'alpface'
print(a['name'], a['age'])
#这里打印的是 'p1' 20, alpface 20
#可见__getitem__使实例可以像字典一样访问
#__setitem__ 设置容器中指定元素的行为，相当于self[key] = value

# __getattr__(self,name)，__getattribute__(self,name)，__setattr__(self,name,value)，__delattr__(self,name)，__get__(self,instance,owner)，__set__(self,instance,value)，__delete__(self,instance)
'''
__getattr__ 定义当用户试图访问一个不存在属性的时候的行为

　　__setattr__ 定义当一个属性被设置的时候的行为

　　__getattribute__ 定义当一个属性被访问的时候的行为
'''

class Persion2(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._registry = {
            'name': name,
            'age': age
        }
    def __getattr__(self, item):
        print("don't have the attritube" + item)
        return False

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattribute__(self, item):
        # 注意此处不要用 self.__dict__[item]
        # 因为self.__dict__ 依然会被__getattribute__拦截，这样会进入死循环
        return object.__getattribute__(self, item)

b = Persion2('p2', 20)
print(b.mm)  # 打印 don't have the attritubehh，因为没有mm这个属性
a.mm = 'mmmm' # 这里设置该属性值为'mmmm'
print(a.mm)  # 这里打印mmmm

'''
__delattr__ 定义当一个属性被删除的时候的行为

　　__get__  定义当描述符的值被取得的时候的行为

　　__set__ 定义当描述符的值被设置的时候的行为

　　__delete__ 定义当描述符的值被删除的时候的行为
'''
class Descriptor(object):
    def __init__(self):
        self.des = None
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.des, None)

    def __set__(self, instance, value):
        instance.__dict__[self.des] = value

class Persion3(object):
    des = Descriptor()  # 这里Descriptor就是一个描述符类

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._registry = {
            'name' : name,
            'age' : age
        }
p3 = Persion3('p3', 20)
p3.des = 10 #这里会调用Descriptor的__set__方法
print(p3.des) #这里会调用Descriptor的__get__方法



