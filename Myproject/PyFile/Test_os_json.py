import os
import json

def t1():
    print(os.getcwd())
    filedir  = os.path.join(os.getcwd(),'filedir')
    if not os.path.isdir(filedir):
        os.mkdir(filedir)
    file = os.path.join(filedir,'file.json')
    with open(file,'w')as f:
        pass
    try:
        with open(file,'r')as f :

            dicFile =json.load(f)
    except:
        print("open file error")
    else:
        print("oepn file successful")


if __name__ == '__main__':
    t1()