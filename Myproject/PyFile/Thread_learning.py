import os
import sys
import threading
import time
import queue

def func(id , name , count):
    for i in range(count):
        print('id:',id)
        print('name:',name)



class Mythread(threading.Thread):
    def __init__(self,threadid ,threadname ,count):
        threading.Thread.__init__(self)
        self.tid   = threadid
        self.tname  =threadname
        self.count = count
    def run(self):
        func(self.tid,self.tname,self.count)



def main():
    t1 = Mythread(1,'thread :1',5)
    t2 = Mythread(2 , "thread :2",7)
    threads = []
    threads.append(t1)
    threads.append(t2)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

#___测试上锁操作 ____________________


exitflg =0

class MyQueuethread(threading.Thread):
    def __init__(self,threadid ,threadname ,q):
        threading.Thread.__init__(self)
        self.tid   = threadid
        self.tname  =threadname
        self.q = q
    def run(self):
        print('Start thread:',self.tname)
        process_data(self.tname,self.q)


def process_data(threadname,q):
    while not exitflg:
        threading.Lock().acquire()
        if not q.empty():
            data =q.get()
            threading.Lock().release()
            print('thread name:',threadname)
        else:
            threading.Lock().release()
        time.sleep(1)
threadlist = ['thread 1','thread 2','thread 3']
namelist  =['one','two','three','four','five']
workQue= queue.Queue(10)
threads=[]
QLock =threading.Lock()

def Test_Q():
    for id  , tname in enumerate(threadlist):
        thread  =MyQueuethread(id,tname,workQue)
        thread.start()
        threads.append(thread)

    QLock.acquire()
    for word in namelist:
        workQue.put(word)
    QLock.release()
    for t in threads:
        t.join()
    print('exit main ')




if __name__=="__main__":
    Test_Q()



