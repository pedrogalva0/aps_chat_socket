import sqlite3

class StorageManager:
    def __init__(self, db_path='chat.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensagens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                remetente TEXT NOT NULL,
                conteudo TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def salvar_mensagem(self, remetente, conteudo, timestamp):
        self.cursor.execute('''
            INSERT INTO mensagens (remetente, conteudo, timestamp) VALUES (?, ?, ?)
        ''', (remetente, conteudo, timestamp))
        self.conn.commit()