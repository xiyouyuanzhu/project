import pexpect
import os

def  IsAble():
    file =os.path.join(os.getcwd(),'test.log')
    with open(file,'a')as f :
        chiild =pexpect.spawn('/bin/bash',['-c','source /etc/profile && ls -l '] ,logfile=f,encoding='utf-8')
        chiild.expect(pexpect.EOF)
    with open(file,'r')as f :
        data = f.read()
        print(data)

if __name__ == '__main__':
    IsAble()
