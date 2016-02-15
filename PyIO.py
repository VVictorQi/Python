#对于基础的python读写文件，我们要知道python是c语言编写的，虽然具有各种风骚的 特性，但是骨子里还是摆脱不了C语言是他爹的事实
#读写文件基本上还是C语言那一套 ， write read   都是后期采用系统调用
#不过在这个基础上我们应该，相信青出于蓝而胜于蓝。
#举例说明： 为了不每一次都要关闭文件有了with的方法
# with open('README.md','r') as f:
#     print(f.read())
import os
print(os.name)
print(os.path.abspath('.'))

os.rmdir('./test')