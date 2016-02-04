#!/usr/include/env python3
#-*-coding: utf-8 -*-
'a test module '
__author__='Victor Qi'

import sys
def test():
    args=sys.argv
    if len(args)==1:
        print("Hello world")
    elif len(args)==2:
        print("Hello %s!"%args[1])
    else:
        print("Too many argument")
if __name__=='__main__':
    test()

#安装第三方模块例如图形处理模块Pillow只支持到2.7
from PIL import  Image
im=Image.open("1.png")
print  (im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')

