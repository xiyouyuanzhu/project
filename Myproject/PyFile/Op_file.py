import os
import sys
import zipfile
import threading
#深度遍历文件， 调用os.listdir
path = '/home/zhuzi166/Desktop/git/Myproject'
def deepSearch(path ,list):
    threads =[]
    files = os.listdir(path)
    for file in files:
        file =path+'/'+file
        print(file)
        if os.path.isdir(file):
            path = path
            t =threading.Thread(target=deepSearch,args=(path,list))
            t.start()
            threads.append(t)
            deepSearch(path,list)
        else:
            list.append(file)
    for thread in threads:
        thread.join()
    print(list)
def t1():
    list=[]
    deepSearch(path,list)


if __name__ == '__main__':
    t1()

