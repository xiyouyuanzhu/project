import re



def t1():
    str = '<H1>hello123</H1>'
    reg =re.compile(r'<.*?>')
    data = reg.search(str).group()
    print(data)




def main():
    t1()
if __name__ == '__main__':
    main()