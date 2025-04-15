import socket
import threading

class ClientNetwork:
    def _init_(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))

    def send_message(self, msg):
        self.client_socket.send(msg.encode('utf-8'))

    def receive_messages(self, callback):
        def loop():
            while True:
                try:
                    msg = self.client_socket.recv(1024).decode('utf-8')
                    callback(msg)
                except:
                    break
        threading.Thread(target=loop, daemon=True).start()