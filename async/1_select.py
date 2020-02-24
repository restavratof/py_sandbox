import socket
from select import select

to_monitor = []

srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv_socket.bind(('localhost', 5001))
srv_socket.listen()


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    to_monitor.append(client_socket)

def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = 'Hello World\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()

def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])  # read, write, errors

        for sock in ready_to_read:
            if sock is srv_socket:
                accept_connection(srv_socket)
            else:
                send_message(sock)

if __name__ == '__main__':
    to_monitor.append(srv_socket)
    # accept_connection(srv_socket)
    event_loop()
