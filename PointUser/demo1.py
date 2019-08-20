import os
import pwd
import subprocess
import sys
import pexpect

def demote(user_uid, user_gid):
    def result():
        os.setgid(user_gid)
        os.setuid(user_uid)
    return result


def exe_cmd(USER,SHELL):
    try:
        pw_record = pwd.getpwnam(USER)
    except Exception as e:
        print('usr is not found',e)

    user_name      = pw_record.pw_name
    user_home_dir  = pw_record.pw_dir
    user_uid       = pw_record.pw_uid
    user_gid       = pw_record.pw_gid
    env = os.environ.copy()
    env[ 'HOME'     ]  = user_home_dir
    env[ 'LOGNAME'  ]  = user_name
    env[ 'PWD'      ]  = user_home_dir
    env[ 'USER'     ]  = user_name
    cwd = user_home_dir

    cmd = SHELL
    p = subprocess.Popen(cmd,preexec_fn=demote(user_uid, user_gid), cwd=cwd, env=env)



def t1():
    user = 'test_user'
    cmd = 'whoami'
    exe_cmd(user, cmd)

def  IsAble():
    p=subprocess.Popen(args='su zhuzi166 ; env',shell=True)
    data =   p.stdout.read().decode('utf-8')
    print(data)
def t2():
    auser = pwd.getpwall()
    print(auser)
def t3():
    data = os.system('ls /home/zhuzi166/')
def main():
    t3()



if __name__ == '__main__':
    main()

