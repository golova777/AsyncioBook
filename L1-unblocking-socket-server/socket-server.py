import selectors
import socket
from array import array
from selectors import SelectorKey
from typing import List, Tuple


selector = selectors.DefaultSelector()

server_socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)

    if len(events) == 0:
        print("no events. i'll wait some time more...")

    for event, _ in events:
        event_socket = event.fileobj

        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f"got request for connection from {address}")
            selector.register(connection, selectors.EVENT_READ)

        else:
            data = event_socket.recv(10)

            if b'\r\n' in data:
                # Manage End Of Data '\r\n'
                # just terminate client socket
                selector.unregister(event_socket)
                event_socket.close()
                continue

            if data == b'':
                # Manage no data input
                # just terminate client socket
                selector.unregister(event_socket)
                event_socket.close()
                continue

            print(f"Got data: {data}")
            event_socket.send(data)


