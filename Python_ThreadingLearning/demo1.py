from threading import Thread
import threading
import time
def say(name):
    time.sleep(2)
    print('{} say hello'.format(name))
if __name__ == '__main__':
    t = Thread(target=say,args=('yuanzhu',))
    t.setDaemon(True)
    t.start()
    print('main')
    print(t.is_alive())

