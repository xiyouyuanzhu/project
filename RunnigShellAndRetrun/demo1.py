import os
import subprocess
def  TestReturn():
    res = os.system('/bin/bash ./run.sh && echo $ ?')
    #res=os.system('ls -l')
    print('res_code=',res)
def  t2():
    cmd='/bin/bash ./run.sh && echo $ ?'
    #p=subprocess.Popen(args=cmd,stdout=)
    r=subprocess.call(args=cmd,shell=True,cwd='/home/zhuzi166/workspace/project/RunnigShellAndRetrun')
    print("r=",r)
if __name__ == '__main__':
    t2()