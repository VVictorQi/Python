import socket,threading,time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',18800))
s.listen(5)
print("staring listen the port ...")
print("waiting for connecting...")


def tcplink(sock,addr):
    print("Accept new connection from %s %s..."%addr)
    sock.send(b'Wecome my home!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello %s!'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print("Connecting from %s:%s closed"%addr)

while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink, args=(sock, addr))
    t.start()