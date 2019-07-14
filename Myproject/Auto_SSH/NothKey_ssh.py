import paramiko
def NoneKey():
    ssh  = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='192.168.136.129',username='zhuzi166')
    i ,o, e  = ssh.exec_command('ls ')
    print(o.read().decode('utf-8'))


if __name__ == '__main__':
    NoneKey()