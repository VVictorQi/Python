# import os
# print("Process (%s) start ..."%os.getpid())
# pid=os.fork()
# if pid==0:
#     print(" I am child Process %s and my parent is %s"%(os.getpid(),os.getppid()))
# else :
#     print("I %s just create a child process %s"%(os.getpid(),pid))

#这段代码在windows中无法运行，因为window建立进程不是这种方法fork在unix linux mac下可以完美运行

# 兼容windows下多进程环境
from multiprocessing import Process
import os



def run_proc(name):
    print("Run child process %s %s "%(name,os.getpid()))
if __name__=='__main__':
    print("Parent Process %s "%os.getpid())
    p=Process(target=run_proc,args=('test',))
    print("Child process will start")
    p.start()
    p.join()
    print('Child priocess end')

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步

#对于启动大量进程时采用进程池的方法控制子进程的数量

import multiprocessing
import os ,time,random,subprocess
def long_time_task(name):
    print("Run task %s (%s)"%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds'%(name,(end-start)))

if __name__=='__main__':
    print('Parent Process %s '%os.getpid())
    p=multiprocessing.Pool(10)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done')


#子进程
import subprocess
print('$nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])
print('EXIT Code',r)
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


