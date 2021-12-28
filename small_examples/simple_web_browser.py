import socket

# host = 'data.pr4e.org'
host = 'localhost'
# port = 80
port = 9000


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, port))
# cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
cmd = 'GET http://localhost:9000 HTTP/1.1\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
