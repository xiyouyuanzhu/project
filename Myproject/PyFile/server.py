import socket
def server():
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    tupaddr = (host, port)
    # print(tupaddr)
    s.bind(tupaddr)
    s.listen(5)
    while True:
        print("wait ")
        c, addr = s.accept()
        c.send("Hello my name is  server".encode('utf-8'))
        string = c.recv(1024)
        print(string)


if __name__ == '__main__':
    server()
