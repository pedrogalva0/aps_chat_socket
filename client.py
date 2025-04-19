import socket
import logging
import json
from datetime import datetime

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Client:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            logging.info(f"Conectando ao servidor em {self.host}:{self.port}...")
            self.client_socket.connect((self.host, self.port))
            logging.info("Conectado ao servidor!")
        except (ConnectionError, OSError) as e:
            logging.error(f"Erro ao conectar ao servidor: {e}")
            self.client_socket.close()  # Fechar o socket caso a conexão falhe
            raise  # Levanta a exceção para indicar que a conexão falhou

    def send_message(self, message):
        # Criando um dicionário para a mensagem
        msg = {
            "remetente": "Cliente",
            "conteudo": message,
            "timestamp": datetime.now().isoformat()
        }
        try:
            # Convertendo para JSON e enviando
            self.client_socket.send(json.dumps(msg).encode('utf-8'))
            logging.info(f"Mensagem enviada: {message}")
        except (ConnectionError, OSError) as e:
            logging.error(f"Erro ao enviar mensagem: {e}")
            self.client_socket.close()  # Fechar o socket se houver erro
            raise  # Levanta a exceção para indicar que houve erro na comunicação

    def receive_message(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode('utf-8')
                if msg:
                    logging.info(f"Mensagem recebida: {msg}")
                else:
                    break  # Se a mensagem for vazia, sai do loop
            except Exception as e:
                logging.error(f"Erro ao receber mensagem: {e}")
                break  # Se houver erro ao receber mensagem, sai do loop

    def close_connection(self):
        self.client_socket.close()
        logging.info("Conexão fechada.")

if __name__ == '__main__':
    client = Client()
    try:
        client.connect()

        # Enviar e receber mensagens
        while True:
            msg = input("Digite a mensagem para enviar (ou 'sair' para sair): ")
            if msg.lower() == 'sair':
                break
            client.send_message(msg)
            client.receive_message()

    except Exception as e:
        logging.error(f"Erro na comunicação com o servidor: {e}")
    finally:
        client.close_connection()

