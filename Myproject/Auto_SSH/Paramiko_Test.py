import paramiko
import os

def t1():
    host = '192.168.136.129'
    name= 'zhuzi166'
    pwd='Woshiyuanzhu'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,username=name,password=pwd)
    stdin,stdout ,stderr = ssh.exec_command('xhost +')
    cmdresult = stdout.read().decode('utf-8') + stderr.read().decode('utf-8')
    print(cmdresult)
    stdin,stdout ,stderr = ssh.exec_command('firefox')
    cmdresult = stdout.read().decode('utf-8')+stderr.read().decode('utf-8')
    print(cmdresult)
def t2():
    host = '192.168.136.129'
    name = 'zhuzi166'
    pwd = 'Woshiyuanzhu'
    ssh = paramiko.SSHClient()

    pkeyfile  = os.path.expanduser('~/.ssh/id_rsa')
    mykey = paramiko.RSAKey.from_private_key_file(pkeyfile)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=name)

    stdin, stdout, stderr = ssh.exec_command('xhost +')
    cmdresult = stdout.read().decode('utf-8') + stderr.read().decode('utf-8')
    print(cmdresult)
    stdin, stdout, stderr = ssh.exec_command('firefox')
    cmdresult = stdout.read().decode('utf-8') + stderr.read().decode('utf-8')
    print(cmdresult)

if __name__ == '__main__':
    t2()