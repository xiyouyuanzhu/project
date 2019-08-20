import subprocess
import pwd
import logging
import os
def getlloger():
    logger = logging.getLogger("loggingmodule.NomalLogger")
    handler = logging.FileHandler("/home/zhuzi166/workspace/project/DebugLearn/t1.log")
    formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

def t1():
    logger = getlloger()
    p = subprocess.Popen(args='env',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout = p.stdout.read().decode('utf-8')
    logger.info(stdout)



if __name__ == '__main__':
    t1()