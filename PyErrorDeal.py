#断言
def foo(s):
    n=int(s)
    assert n!=0,'n is zero '
    return 10/n
def main():
    foo('0')
#断言可以通过python filename -o 来关闭assert：这样处理的结果就是assert被当做pass处理

#logging 输出到文件 ，跟shell脚本相比就是相当于重定向 1&2>filename
import logging
logging.basicConfig(level= logging.INFO)
s='0'
n=int(s)
logging.info('n=%d'%n)
print(10/n)
#通过pdb方式处理，这是python的调试器，相当于gdb，n是单步调试，p valuename 查看变量值 q结束
#设置断点调试可以利用
import pdb
pdb.set_trace()
#最后利用最常用的IDE，例如epliise Pycharm等都可以


#对于单元测试

class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Dict' object has no attribute %s'"%key)
    def __setattr__(self, key, value):
        self[key]=value

#编写单元测试部分
import unittest
class TestDict(unittest.TestCase):
    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
    def test_key(self):
        d=Dict()
        d.key='value'
        self.assertEqual(d.key,'value')
    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')
    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(KeyError):
            value=d['empty']
    def test_attrerror(self):
        d=Dict()
        with self.assertRaises(AttributeError):
            value=d.empty
if __name__ == '__main__':
    unittest.main()
# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
# 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。
#后续的还有集成测试，白盒测试，黑盒测试，各种方法，前后大约有二十种方法


#文档测试，在java中也有这样的方法，这是测试的一种，在注释中，java有一个专门的文档注释
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()