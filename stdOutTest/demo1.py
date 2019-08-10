import sys
import threading
import time


out=sys.stdout
f =open('t.log','a')
sys.stdout=f
sys.stderr=f

class flushThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            f.flush()
            time.sleep(3)



def t1():
    p=flushThread()
    p.setDaemon(True)
    p.start()

    i=1
    while True :
        if i==30 :
            print("Runing test {}".format(i))
            time.sleep(1)
            i=i+1
        else:
            break
    sys.stdout=out
    print("Fuc end ")
if __name__ == '__main__':
    t1()