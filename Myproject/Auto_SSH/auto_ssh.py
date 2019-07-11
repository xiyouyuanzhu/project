import pexpect


# 编写脚本实现自动化ssh 登录，借助pexpect 模块。
#


'''
Just do it:
https://www.cnblogs.com/jiaoyu121/p/7027694.html

Just do it:
https://www.cnblogs.com/jianghongchao/p/10803184.html

https://www.jb51.net/article/156239.htm

'''
def sendcommand(cmd,child):
    print('sendcommand running')
    child.sendline('{}  \n'.format(cmd))
    print(child.before())
    print('send command running end')

def connect(cmd,pwd):
    child = pexpect.spawn(cmd)
    i = child.expect(['.*password.*','.*continue.?',pexpect.EOF,pexpect.TIMEOUT])
    if i==0:
        child.sendline('{}\n'.format(pwd))
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
    child.sendline('{}\n'.format('export DISPLAY=:0'))


    child.sendline('{}\n'.format('xhost +'))

    child.sendline('{}\n'.format('firefox'))

    try:
        sendcommand('gedit t.txt',child)
    except:
        print('running gedit t.txt error')
        exit(1)







def t1():
    name = 'zhuzi166'
    host = '192.168.136.129'
    psw = 'Woshiyuanzhu'
    connect('ssh  {}@{}'.format(name, host), psw)



if __name__ == '__main__':
    t1()