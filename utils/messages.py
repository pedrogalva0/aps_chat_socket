import json
import datetime

class Message:
    def _init_(self, remetente, conteudo, timestamp=None):
        self.remetente = remetente
        self.conteudo = conteudo
        self.timestamp = timestamp or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_json(self):
        return json.dumps({
            "remetente": self.remetente,
            "conteudo": self.conteudo,
            "timestamp": self.timestamp
        })

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Message(data['remetente'], data['conteudo'], data['timestamp'])