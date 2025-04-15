import tkinter as tk
from client.network import ClientNetwork
from utils.messages import Message

class ChatGUI:
    def _init_(self):
        self.rede = ClientNetwork()
        self.rede.connect()

    def iniciar_interface(self):
        self.window = tk.Tk()
        self.window.title("Chat do Inspetor")

        self.txt_area = tk.Text(self.window, height=20, width=50)
        self.txt_area.pack()

        self.input_msg = tk.Entry(self.window, width=50)
        self.input_msg.pack()

        self.btn_send = tk.Button(self.window, text="Enviar", command=self.enviar)
        self.btn_send.pack()

        self.rede.receive_messages(self.exibir_mensagem)
        self.window.mainloop()

    def enviar(self):
        conteudo = self.input_msg.get()
        mensagem = Message(remetente="Inspetor", conteudo=conteudo)
        self.rede.send_message(mensagem.to_json())
        self.input_msg.delete(0, tk.END)
        self.exibir_mensagem(mensagem.to_json())

    def exibir_mensagem(self, json_str):
        msg = Message.from_json(json_str)
        self.txt_area.insert(tk.END, f\"{msg.timestamp} - {msg.remetente}: {msg.conteudo}\\n\")