#当出现函数的时候世界的曙光出现了，重复的事情变得简单
#python提供了很多内置的函数供开发者使用，方便了管理，对于API的使用，可以使用help(命令)形同于linux下的man手册

def Whichbig(a,b,c):
        x=(max(a,b,c))
        return x
#投机取巧打个包装，当然做一个比较还是很简单的没事试试吧
#对于一个空函数
def MyNull():
    pass
#意味着什么都不做，在以后的大型编程中可能是意味着在这里留一个接口，供后续使用
import math
#是一个导包的过程形同于C的#include又有所不同，真要说像的话是和java的packge是一样的 道理
#返回多个值，当然在外面你的类型要是一样，要可以接受这些返回值例如元组，列表。这在爬虫中经常使用
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple

#关于函数的参数，有这么几点注意，函数可以是多个参数，从无到无穷不等，函数也可以是默认参数，要注意的是默认参数，必须是不可变参数，也就是我们说的常量
    # ，变量有太多可变性，具有不可预知性。
def add_list(L=[]):
    L.append('ONE')
    return L
#这是有错的，会出现不可预知的后果，因为不能总是得到你想要看到的结果，原因就是因为参数是不可预知的

#对于可变参数的问题，有这么几种解决方法，一个是给函数中传递list或者tuple对象，一种是函数参数对象添加*号，例如*nums,这样的感觉就是C中的指针但是在python中是没有指针的
#这样就解决了可变长参数的问题


def GetNums(*nums):
    print (nums[0])
GetNums(0)
#解释器会自动将参数合成为一个tuple
#当你使用关键字作为参数时，传递会自动合成dict，例如
def MyFamilyMem(name,age,**Familynote):
    print(name,age,Familynote)
MyFamilyMem("Bob",15,sex='boy')
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
#
# 以及调用函数时如何传入可变参数和关键字参数的语法：
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
# 定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数

##对于递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
#典型的 斐波那契函数，对于递归函数时通过不停的压栈来运行的，栈的空间有限，不能无限递归。和调用函数相同又不相同解决栈溢出的方法是为递归
#尾递归就相当于将其变成循环函数，调用一次释放一次，所以不会出现栈溢出的情况

def factextern(n):
    return fact_iter(n,1)
def fact_iter(num,prodect):
    if num==1:
        return prodect
    return fact_iter(num-1,num*prodect)
#在返回的时候减少了调用栈的过程

# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出
# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题



#python崇尚的极简原则。高级特性
#1、切片。对于一个列表中有多个元素，我们想提取其中第n到m个怎么办？for循环遍历算一种，一个一个输出，也算提取，但是这样是否麻烦呢？
#去一两个元素，你说一下两下的提取确实很方便，要是有50多，100多呢甚至更多。要是列表中有1000个呢for循环也浪费了那么多次轮询，当然额，可以使用条件判断终止循环。但是明明可以一行代码解决，浪费那么多体力干什么，哈哈，这就是切片
Listone=[]
for i in range (1000):
    Listone.append(i)
print (Listone)
Listone=list(range(100))#初始化的简便方式
print(Listone[2:50])#这就是切片
Listone[:50]#省略了开头
Listone[20:]#省略了结尾
print (Listone[20::2])
print (Listone[-10:])
tupleone=tuple(range(100))
print(tupleone[10:15])#对于列表和元镞都可以使用切片技术

#对于可迭代对象，形同于for循环中变量的 增长依赖上一次 的结果，在数值计算这门课上有相应的介绍与学习。有兴趣可以去学习
for x,y in ((1,1),(2,4)):
    print (x,y)


#列表生成式
#一个列表想要生成1..100的x^2,for 循环依旧可以，但是还是比较繁琐
L=[]
for i in range(100):
    L.append(i*i)
#也可以这样干
[x*x for x in range (199)]
#甚至可以在此基础上筛选想要的结果
Listtwo=[i*i for i  in range(10,50,2) if i%5==0]
print (Listtwo)
#在此基础上还可以套用循环，多层循环，生成表达式。但是一般不超过三层循环，这样违背了简单的 原则。可以将他们分开来写。当然一行代码能完成的事，也是很酷的

# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象
#对于生成器和迭代器，其实迭代器算是生成器 的一种高级抽像，因为生成器的思想中也是迭代
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现


#高阶函数的使用
#高阶函数 的思想是，函数也可以作为函数的变量和参数使用
intA=max(1,2,3,4,5,6)
maxA=max
intB=maxA(1,4,5,6,7,8)
print(intA,intB)
#结果是一样的

def add_My(x,y,f):
    return f(x^2,y)+f(y^2,x)
print (add_My(10,2,max))

# map()作为高阶函数，事实上它把运算规则抽象map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list

def f(x):
    return x*x
r=map(f,[1,20,40,5,3,2,3,42])
list (r)

#对于reduce
from functools import reduce
def add_reduce(x,y):
    return x+y
a=reduce(add_reduce,[1,2,7,4,3,5])
print (a)
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

#对于filter 就相当于map加上了筛选功能
def   is_palindrom(n):
     return n == int(str(n)[::-1])#进行一个回文数的判断，就是将整数转化为字符串，然后进行一一判断

#对于高阶函数sorted ，内置函数作为排序使用，还可以接受自定义键值来排序，用sorted()排序的关键在于实现一个映射函数。

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sort_byname(t):
    return t[0]
def sort_byscore(t):
    return t[1]
La=sorted(L,key=sort_byname)
print (La)
Lb=sorted(L,key=sort_byscore,reverse=1)
print(Lb)


# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return  fs

#对于匿名函数lambda 不能有return返回值，基本上都是一个表达式
def add(x,y):
    return lambda : x^3+y^3
#python对lambda的支持有限，相反对于C++，js之类的语言反倒是经常使用lambda已经在C++11 规范里面添加现在是2016年，其使用方法和范围得到了大大的扩散



#对于装饰器函数u，采用了设计模式中的 装饰模式的影响
#其本质上装饰器就是一个返回函数的高阶函数。在动态添加功能的时候，又不能修改原有代码，保持原有兼容性，又要添加新功能，所以就有了装饰器，在不修改原有的基础上添加功能
# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。
# Python的decorator可以用函数实现，也可以用类实现。decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#对于functool中的偏函数模块而言，其目的是为了简化函数
int2=functools.partial(int,base=2)
numone=int2('1001')
print(numone)

