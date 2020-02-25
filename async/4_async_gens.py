import socket

def server():
    srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_socket.bind(('localhost', 5001))
    srv_socket.listen()

    while True:
        client_socket, addr = srv_socket.accept()   # read
        print('Connection from', addr)
        client(client_socket)


def client(client_socket):
    while True:
        request = client_socket.recv(4096)   # read

        if not request:
            break
        else:
            response = 'Hello World\n'.encode()
            client_socket.send(response)    # write

    print('Outside inner while loop')
    client_socket.close()

server()
