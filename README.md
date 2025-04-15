# aps_chat_socket

📁 projeto_chat/
├── 📁 server/
│   ├── server_main.py         # Inicia o servidor e escuta conexões
│   ├── client_handler.py      # Lida com cada cliente conectado
│   └── storage.py             # Lógica de armazenamento (log, SQLite, etc.)
│
├── 📁 client/
│   ├── client_main.py         # Interface principal do cliente
│   ├── network.py             # Lógica de envio e recebimento de mensagens
│   └── gui.py                 # Interface gráfica (Tkinter)
│
├── 📁 utils/
│   └── messages.py            # Definições e formatação de mensagens
│
└── README.md                  # Explicação do projeto 