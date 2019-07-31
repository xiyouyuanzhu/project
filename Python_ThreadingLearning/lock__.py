import threading
from threading import Thread
import os
import time

def work():
    global n
    temp =n
    time.sleep(n)
    n=temp-1

if __name__ == '__main__':
    n =100
    