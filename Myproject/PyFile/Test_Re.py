import  re
#测试匹配linux中路径的正则表达式方法


##   /opt/pycharm-community-2019.1.3/
def test_Re():
    #\w匹配字母数字下划线
    #？匹配0或多个
    reg = re.compile(r'(/[\w,\.-]+/?)+')
    str = '/opt/pycharm-community-/1.23'
    data = reg.fullmatch(str)
    print(data)
def t1():
    str  ='.'
    reg = re.compile(r'[a-z,\.]')
    data =reg.search(str)
    print(data)


def main():
    test_Re()

if __name__ == '__main__':
    #t1()
    main()