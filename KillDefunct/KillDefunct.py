import os

#思路是，通过人机交互，找到僵尸进程的父进程，讲僵尸进程转化为孤儿进程进行正确处理
def KillDefunct():
    data = os.popen('ps -ef |grep py|grep -v grep').read()
    listdata = data.split('\n')
    print(listdata)
    TempKillList = []
    for line in listdata:
        templist =[]
        listline = line.split(' ')
        for  ldata in listline:
            try:
                num = int(ldata)
            except:
                continue
            if isinstance(num,int):
                templist.append(num)
        TempKillList.append(templist)
    KillList = []
    for list in TempKillList:
        if len(list)>=3:
            KillList.append(list[1])
    for pid in KillList:
        os.system('kill -9 {}'.format(pid))
def main():
    KillDefunct()
if __name__ == '__main__':
    main()