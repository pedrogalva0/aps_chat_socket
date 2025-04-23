import asyncio
import websockets
import json

clients = set()

async def handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            print(f"Mensagem recebida: {data}")
            # Criando tarefas explicitamente
            tasks = [asyncio.create_task(client.send(message)) for client in clients]
            if tasks:
                await asyncio.wait(tasks)
    except websockets.ConnectionClosed:
        print("Conexão encerrada")
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 6789):
        print("Servidor WebSocket rodando em ws://localhost:6789")
        await asyncio.Future()  # Mantém o servidor rodando

if __name__ == "__main__":
    asyncio.run(main())
