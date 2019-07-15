import psutil

def Use():
    for pid in psutil.pids():
        data = psutil.Process(pid=  pid)
        print(data)



# def  FindPid():
#     # file  .pid 文件
#     with open(file,'r')as f :
#         pid = f.read()  #会得到其进程号
#


if __name__ == '__main__':
    Use()
