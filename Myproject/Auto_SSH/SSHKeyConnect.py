import paramiko

def sshConnect():
    key = paramiko.RSAKey.from_private_key_file('/home/zhuzi166/.ssh/id_rsa')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(username='zhuzi166',pkey=key,hostname='127.0.0.1')
    i,o,r   = ssh.exec_command('ls')
    print(o.read().decode('utf-8'))
    print(r.read().decode('utf-8'))

def main():
    sshConnect()

if __name__ == '__main__':
    main()
