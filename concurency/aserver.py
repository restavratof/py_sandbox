# server.py
# Fib microservice

from socket import *
from fib import fib
from collections import deque
from select import select
from concurrent.futures import ProcessPoolExecutor as Pool

pool = Pool(4)

tasks = deque()
to_recv = {}  # Mapping sockets -> tasks (generators)
to_send = {}
to_future = {}

future_notify, future_event = socketpair()


class AsyncSocket(object):
    def __init__(self, sock):
        self.sock = sock

    def recv(self, maxsize):
        yield 'recv', self.sock
        return self.sock.recv(maxsize)

    def send(self, data):
        yield 'send', self.sock
        return self.sock.send(data)

    def accept(self):
        yield 'recv', self.sock
        client, addr = self.sock.accept()
        return AsyncSocket(client), addr

    def __getattr__(self, name):
        return getattr(self.sock, name)


def future_done(future):
    tasks.append(to_future.pop(future))
    future_notify.send(b'x')

def fututre_monitor():
    while True:
        yield 'recv', future_event
        future_event.recv(100)

tasks.append(fututre_monitor())

def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        yield 'recv', sock
        client, addr = sock.accept()
        print("Connection", addr)
        tasks.append(fib_handler(client))

def fib_handler(client):
    while True:
        yield 'recv', client
        req = client.recv(100)
        if not req:
            break
        n = int(req)
        future = pool.submit(fib,n)
        yield 'future', future
        result = future.result()     # Blocks
        resp = str(result ).encode('ascii') + b'\n'
        yield 'send', client
        client.send(resp)
    print('Closed')

def run():
    while any([tasks, to_recv, to_send]):
        while not tasks:
            # No active tasks to run
            #wait for I/O
            can_recv, can_send, [] = select(to_recv, to_send, [])
            for s in can_recv:
                tasks.append(to_recv.pop(s))
            for s in can_send:
                tasks.append(to_send.pop(s))

        task = tasks.popleft()
        try:
            why, what = next(task)  # Run to the yield

            if why == 'recv':
                # Must go wait somewhere
                to_recv[what] = task
            elif why == 'send':
                to_send[what] = task
            elif why == 'future':
                to_future[what] = task
                what.add_done_callback(future_done)
            else:
                raise  RuntimeError("ARG!")

        except StopIteration:
            print('task done')

tasks.append(fib_server(('',25000)))
run()

