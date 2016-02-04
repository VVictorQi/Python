#python基础
print ("gello world")#其实还是调用系统调用python底层是C语言
#文本编辑器写Python程序，然后保存为后缀为.py的文件，就可以用Python直接运行这个程序本实例采用PyCharm
print ("strA","strB","strC")#连接字符串

#类似于scanf的语句
# name=input("Please input your name :")
# print (name)
#对于Python基础
#Python大小写敏感，缩进更敏感，这样是为了保证程序员的良好风格
#python支持 整数、浮点数、字符串、布尔值、空值、常量这些数据类型，在基础上和C语言系列是一致的
ord('A')#将字符转化为相应的编码
chr(25991)#将编码转换为相应的字符
print ("中文输出")
Miss='Miss'
print("Dear Jeson ,I %s you"%Miss)# 形似于C语言 的printf函数

#list  tuple列表和元组
#列表和数组一样，可以改变元素中的内容，但是元组不一样，不可以改变元组中的元素。
#  当然这也不是一成不变，tuple中的不变是指永远不改变指向，若指向为列表，其列表的元素是可变的
listA=['Apple',34,'76']
print (listA)
print ( listA[2],listA[-1])
tupleA=("hello ","My","world",listA)
print (tupleA,tupleA[2])
tupleA[3][2]="I lovw you "

print(tupleA)
#tuple[1]=" i am wrong "这是错的 不可以改变

#条件判断举个例子

myscore=int(input("我的成绩是这么多%d"))#在这里进行强制类型转换但是在这里没有考虑更多因素例如输入字母什么的，要进行边界检测哦
if myscore<60:
    print("年轻人啊 ，你这分数有危险啊")
elif 60<=myscore<80:
    print("值的鼓励，但会还需要加油")
elif 80<=myscore<100:
    print("么么么哒")
else:
    print("哪里来的妖孽，乱输东西")
#具体就这么点东西
#对于循环语句，其实就是　for   while 这两个

for i in range(10):
    print (i)
i=100
while i>10:
    i-=10
    print (i)


# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#
# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而增加；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
#
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
#对于字典和集合有其利用的场所，在这些场所利用字典和集合是非常方便的，键值对应，例如在一个字典程序中，查找一个单词，写出一个例句和意思


dictA={'Bob':15,'Jeson':24}
print("大家好我是Bob,我今年%d"%dictA['Bob'])


setA=set([1,1,1,2,2,34,4,5,2,54,3,6,3,65,32])
print(setA)
setA.add(15)
setA.remove(1)
print(setA)
#python保证了不可变对象本身永远是不可变的

stra='abc'
strb=stra.replace('a','A')
print(stra,strb)