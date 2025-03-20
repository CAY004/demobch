from flask import Flask, request, jsonify
import socket
import threading
import json

class P2PNetwork:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.nodes = set()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"Listening on {self.host}:{self.port}")

    def start(self):
        threading.Thread(target=self.listen_for_connections).start()

    def listen_for_connections(self):
        while True:
            client_socket, address = self.server.accept()
            print(f"Connection from {address} has been established.")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.process_message(json.loads(message))
            except Exception as e:
                print(f"Error: {e}")
                break
        client_socket.close()

    def process_message(self, message):
        if message['type'] == 'new_node':
            self.nodes.add(message['node'])
            print(f"New node added: {message['node']}")

    def broadcast(self, message):
        for node in self.nodes:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect(node)
                    sock.sendall(json.dumps(message).encode('utf-8'))
            except Exception as e:
                print(f"Could not connect to {node}: {e}")

    def add_node(self, node):
        self.nodes.add(node)
        self.broadcast({'type': 'new_node', 'node': node})

if __name__ == "__main__":
    network = P2PNetwork(port=5001)  # Change port as needed for different nodes
    network.start()