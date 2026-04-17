import asyncio, websockets



async def enviar(ws):
    pass


async def receber(ws):
    pass


async def main(host, porta):
    uri = f'ws://{host}:{porta}'
    async with websockets.connect(uri) as ws:
        print(f'Conectado em {host}:{porta}')
        asyncio.gather(enviar(ws), receber(ws))
