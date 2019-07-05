
#脚本目的为给传输的消息添加头部 ，
#定义头部的格式为：第一位为消息的标志b'\x70'
#第3位和第4位表征消息的bit长度 ，采用小端存储 ，低位在前，高位在后，
#第2位为校验位，为3,4位的亦或

bytedata ='我的名字叫xxx'.encode('utf-8')

#构造16进制小端模式表示，其中INTTYPE 此处为16 ,也可以为8,32
def ConvertInt2Byte(intlenbyte,INTTYPE):
    strhexlen=hex(intlenbyte)[2:]
    remainlen  =INTTYPE//4 -len(strhexlen) ###切记   remain  中的  <INTTYPE>//4

    for i in range(remainlen):
        strhexlen='0'+strhexlen
    Bytehexlen=bytes().fromhex(strhexlen)

    #低位 置前
    b=b''
    for i in range(INTTYPE//8):
        b=Bytehexlen[i:i+1]+b


    return b


def WrapMsg(bytedata):

    if not isinstance(bytedata,bytes):
        print('Input data error')
        return 1
    bytelen = len(bytedata)
    ByteNumber =ConvertInt2Byte(bytelen,16)
    print('ByteNumber=',ByteNumber)
    checkflg = ByteNumber[0]^ByteNumber[1]
    targetdata = 'p'.encode('utf-8')+bytes((checkflg,))+ByteNumber+bytedata
    return targetdata


def OpTargetdata():
    byteTargetData = WrapMsg(bytedata)
    if len(byteTargetData)>4:
        if byteTargetData[0]==112 and byteTargetData[1]==byteTargetData[2]^byteTargetData[3]:
            datalen = byteTargetData[2]+byteTargetData[3]*256
            data = byteTargetData[4:4+datalen]
            print('The data  is ',data.decode('utf-8'))






def t1():
    OpTargetdata()



if __name__ == '__main__':

    t1()