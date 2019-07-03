import getopt
import sys
import os


class Func():
    def __init__(self):
        pass
    def start(self):
        print('start runing')
    def version(self):
        print('version running')
    def help(self):
        print('help running')



def OptGetopt():

    opts ,args = getopt.getopt(sys.argv[1:],'vsh',["version","start","help"])
    f= Func()
    # print(opts)
    # print(args) //选中 crtl +/集体注释
    for option ,other in opts:
        if option in ('-v','--version'):
            f.version()
        elif option in ('-s','--start'):
            f.start()
        elif option in ('-h','--help'):
            f.help()
        else:
            print('error  option')
            exit(1)




def main():
    OptGetopt()

if __name__ == '__main__':
    main()