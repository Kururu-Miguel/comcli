import asyncio, websockets, socket


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


async def handler(ws):
    dados = ws.recv()


async def main(porta):
    host = get_local_ip()
    async with websockets.serve(handler, host, porta):
        print(f'Servidor rodando em ws://{host}:{porta}')
        await asyncio.Future()

