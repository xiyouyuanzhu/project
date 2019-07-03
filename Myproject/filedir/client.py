import socket





def  client():
    s=socket.socket()
    host = socket.gethostname()
    port = 1234
    tupaddr  = (host ,port)
    #print(tupaddr)
    s.connect(tupaddr)
    s.send('my name is client'.encode('utf-8'))
    print(s.recv(1024))




if __name__ == '__main__':
    client()