import pexpect
import pinda
# 编写脚本实现自动化ssh 登录，借助pexpect 模块。
#


'''
Just do it:
https://www.cnblogs.com/jiaoyu121/p/7027694.html

Just do it:
https://www.cnblogs.com/jianghongchao/p/10803184.html

https://www.jb51.net/article/156239.htm

'''


# TIPS  pespect .TIMOUT EOF 是没有after 属性的
def sendcommand(cmd,child):
    print('sendcommand running')
    child.sendline('{}  \n'.format(cmd))
    print(child.before())
    print('send command running end')

def connect1(cmd,pwd):
    child = pexpect.spawn(cmd)
    i = child.expect(['.*password.*','.*continue.?',pexpect.EOF,pexpect.TIMEOUT])
    if i==0:
        print('Enter >>>>psw')

        child.sendline('{}\n'.format(pwd))
        print(child.after)

        #child.sendline('{}\n'.format('export DISPLAY=:0'))

        ##child.sendline('{}\n'.format('xhost +'))

        ##child.sendline('{}\n'.format('firefox'))
        try:
            child.sendline('{}\n'.format('xhost +'))
            print(child.before)
        except :
            print('xhost + error')
            exit(1)
        try:
            child.sendline('{firefox}\n')
        except:
            print('firefox')
            exit(1)

    elif i==1:
        child.sendline('{}\n'.format('yes'))
    elif i==3:
        print('pexpect eof')
        exit(1)
    elif i==4:
        print('Time out')
        exit(1)
    else:
        print('Other error')
        exit(1)

    #ssh zhuzi166@192.168.136.129
    # try:
    #     sendcommand('export DISPLAY=:0 ',child)
    # except:
    #     print('export DISPLAY error')
    #     exit(1)



def connect2(cmd,pwd):
    child = pexpect.spawn(cmd)
    try:
        child.expect('.*password.*',timeout=-1)
        print('____73')
        print(child.before.decode('utf-8'))
        child.sendline('{}\n'.format(pwd))
    except pexpect.EOF:
        print('EOF')
        print(child.before.decode)
    except pexpect.TIMEOUT:
        print('Time out')
    else:
        while True:
            i = child.expect(['.*again.*', pexpect.EOF, pexpect.TIMEOUT], timeout=-1)
            if  i==0:
                print('enter psw again')
                print(child.before.decode('utf-8'))
                child.sendline('{}\n'.format(pwd))

        print(child.before.decode('utf-8'))
    child.sendline('pip install requests')
    child.expect(pexpect.EOF,timeout=-1)
    print(child.before.decode('utf-8'))



#EOF 没哟 after属性

def t1():
    name = 'zhuzi166'
    host = '192.168.136.129'
    psw = 'Woshiyuanzhu'
    #connect2('ssh  {}@{}'.format(name, host), psw)
    child  =pexpect.spawn('ssh {}@{}'.format(name,host))
    i = child.expect(['Welcome','.*password.*','.*continue.?',pexpect.EOF,pexpect.TIMEOUT])
    if i ==0:
        print(child.after.decode('utf-8'))
    elif i==1:
        child.sendline('Woshiyuanzhu\n')
        index =child.expect('Welcome.*')
        print(child.after.decode('utf-8'))
        child.sendline('xhost')
        index = child.expect('')
    else:
        print(child.before.decode('utf-8'))


def t2():
    child = pexpect.spawn('{}\n'.format('pip3 install pinda'))
    i = child.expect(['.*\$',pexpect.EOF,pexpect.TIMEOUT],timeout=-1)
    if i==0:
        print('run successful')
        print(child.before.decode('utf-8'))
    elif i==2:
        print('time out')
        print(child.before.decode('utf-8'))
    elif i==1:
        print('run  finish')
        print(child.before.decode('utf-8'))







if __name__ == '__main__':
    t1()