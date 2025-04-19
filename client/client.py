import socket
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Client:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        logging.info(f"Conectando ao servidor em {self.host}:{self.port}...")
        self.client_socket.connect((self.host, self.port))
        logging.info("Conectado ao servidor!")

    def send_message(self, message):
