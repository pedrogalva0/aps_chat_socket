import socket
import threading
import logging
from server.client_handler import ClientHandler
from server.storage import StorageManager

class Server:
    def _init_(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.clientes = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.storage = StorageManager()

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        logging.info(f"Servidor escutando em {self.host}:{self.port}...")
        while True:
            client_socket, addr = self.server_socket.accept()
            handler = ClientHandler(client_socket, addr, self)
            self.clientes.append(handler)
            thread = threading.Thread(target=handler.run)
            thread.start()

    def broadcast(self, mensagem, remetente):
        for cliente in self.clientes:
            if cliente != remetente:
                cliente.send(mensagem)

    def remover_cliente(self, handler):
        self.clientes.remove(handler)

if __name__ == '_main_':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    servidor = Server()
    servidor.start()