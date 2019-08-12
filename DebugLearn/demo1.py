import logging
import subprocess


def getlloger():
    logger = logging.getLogger("loggingmodule.NomalLogger")
    handler = logging.FileHandler("/home/zhuzi166/workspace/project/DebugLearn/t.log")
    formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
# test
#logger.debug("this is a debug msg!")
#logger.info("this is a info msg!")
def test():
    logger = getlloger()
    logger.debug('hello this is debug')
    logger.error('this is error')
    logger.info('this is info')
    cmd  =''
    data =subprocess.Popen(args='env',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf-8')
    outbuf=data.stdout.read()

    logger.debug(outbuf)





if __name__ == '__main__':
    test()


