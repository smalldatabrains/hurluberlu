import asyncio
import websockets
import json


clients = set() #do not allow duplicate values, list of clients on the server

async def handler(websocket):
    # Register
    clients.add(websocket)
    try:
        async for message in websocket:
            # broadcast to everyone else:
        for client in clients:
            if client != websocket:
                await client.send(message)
    except websockets.ConnectionClosed:
        class classname():
            pass
    finally:
        clients.remove(websocket)
