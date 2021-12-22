# https://docs.python.org/3/howto/sockets.html
# https://stackoverflow.com/questions/8627986/how-to-keep-a-socket-open-until-client-closes-it
# https://stackoverflow.com/questions/10091271/how-can-i-implement-a-simple-web-server-using-python-without-using-any-libraries


from socket import *

host = 'localhost'
port = 9000


def create_server():
    srv_socket = socket(AF_INET, SOCK_STREAM)
    try:
        srv_socket.bind((host, port))
        srv_socket.listen(5)
        while 1:
            (client_soc, address) = srv_socket.accept()

            rd = client_soc.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces[0])
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            client_soc.sendall(data.encode())
            client_soc.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    srv_socket.close()


print(f'Access http://{host}:{port}')
create_server()
