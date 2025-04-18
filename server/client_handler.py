import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import logging
from aps_chat_socket.utils.messages import Message


class ClientHandler:
    def _init_(self, client_socket, address, server):
        self.client_socket = client_socket
        self.address = address
        self.server = server

    def run(self):
        logging.info(f"Conectado a {self.address}")
        while True:
            try:
                msg = self.client_socket.recv(1024).decode('utf-8')
                if not msg:
                    break
                logging.info(f"Mensagem recebida: {msg}")
                message = Message.from_json(msg)
                self.server.storage.salvar_mensagem(message.remetente, message.conteudo, message.timestamp)
                self.server.broadcast(msg, self)
            except:
                break
        self.client_socket.close()
        self.server.remover_cliente(self)

    def send(self, mensagem):
        self.client_socket.send(mensagem.encode('utf-8'))