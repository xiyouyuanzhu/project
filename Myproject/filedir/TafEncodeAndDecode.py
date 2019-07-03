
#目的是实现对String 中特殊字符的编码，根据ASCII十六进制进行编码
#详情参照https://www.cnblogs.com/xingyunblog/articles/3806587.html
#Encode 只针对5中特殊符号进行编码 ，其中为” ‘ % /  \




def TafEncode(String):
    d ={

        '\'':'%27',
        '"':'%22',
        '/':'%2f',
        '\\':'%5c'
    }
    String = String.replace('%','%25')
    for key in d.keys():
        String  = String.replace(key , d[key])
    return String



def TafDecode(String):

    d={
        '%27':'\'',
        '%22':'\"',
        '%2f':'/',
        '%5c':'\\'
    }
    #注意考虑%对程序的影响 ，最后再处理
    for key in d.keys():
        String = String.replace(key,d[key])
    String = String.replace('%25','%')
    return String








def t1():
    string = "AB%/CCCD"
    string = string.replace('A','-')
    print(string)
if __name__=="__main__":
    t1()
