#当机械有了思想，当对象有了灵魂
#面向对象最大的概念就是类和实例，类是抽象的模板
#Python中对于变量数据的隐藏利用开头双下划线
class People(object):
    def __init__(self,name,age,sex):
        self.__name=name
        self.__age=age
        self.__sex=sex
    def printfInfo(self):
        print(self.__name,self.__age,self.__sex)
    def Getname(self):
        return self.__name
    def ChangeName(self,name):
        self.__name=name
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
    def __call__(self):
        print('My name is %s.' % self.name)
#对于类的访问控制，有其构造函数，当需要修改类中变量属性的时候，通过类提供的接口来实现。这就很好的实现了信息隐藏

#对于继承和多态一加多重继承，举个例子吧

class Animal(object):
    def Say(self):
        print("I am a Animal")
class Tiger(Animal):
    def Say(self):
        print("I am a tiger ")
class Lins(Animal):
    def Say(self):
        print ("I am a lins")
class TigerLins(Tiger,Lins):
    def Say(self):
        print("I am a TigerLins")

#并由完美实现了多态。以及单继承和多继承
#对于Python的哲学也是属于万物皆对象，类也不列外，Python中有专门检测判断对象的类型
import types
print(type(123))
print(type(abs))
print(type(TigerLins))
#测试一个对象是否为函数用types
def fn():
    pass
print(type(fn))
print(type(abs))
print(type(lambda x:x*x))
print(type((x for x in range(10))))#这里元素是一个生成器

#isinstance()是判断对象是否是某种类型
print(isinstance(12,int))
zhangsan=People("张三","18","man")#对类进行实例化
zhangsan.printfInfo()
print(isinstance(zhangsan,People))#判断张三是不是人，结果是，哈哈哈

print(isinstance([1,2,3],(list,tuple)))#判断是否为其中的一种类型

#在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。

#一般在类中定义的方法，在实例化的时候进行初始化，但是由于Python是动态语言
#在对象实例后也可以进行现场绑定，为实例绑定变量，为实例绑定方法，甚至临时的为类绑定方法


class Student():
    pass

StuA=Student()
StuA.name="Jeson"
print(StuA.name)


def set_age(self,age):
    self.age=age

from types import MethodType

StuA.set_age=MethodType(set_age,StuA)#动态绑定方法
StuA.set_age(15)
print(StuA.age)
#但是这种方法只对当前实例有效，对其他实例无效，所以实例化的时候我们要给类做一个动态绑定

def set_score(self,score):
    self.score=score

Student.set_score=MethodType(set_score,Student)
StuB=Student()
StuB.set_score(75)
print(StuB.score)

#使用__slots__如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Teacher(object):
    __slots__=('name','age','sex')
#此方法对当前实例有效，对于继承后的子类无效

class CollegeStudent():
    @property#装饰器只读状态
    def score(self):
        return  self._score
    @score.setter#可读写状态
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be int ")#raise一个用来提示错的的关键词
        if value<0 or value>100:
            raise  ValueError("score must be  0 ~100")
        self._score=value

#这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性

print(zhangsan)#<__main__.People object at 0x01AF6370>不好看，在类中用__str__定制


#对于枚举类，挺简单的
from enum import Enum,unique
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6
#@unique 装饰器可以帮助我们检查保证没有重复的键值
for name ,member in Weekday.__members__.items():
    print(name,'=>',member)
# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
# 动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。
# 但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。
# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
