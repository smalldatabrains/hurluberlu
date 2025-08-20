import asyncio
import websockets
import json


clients = set() #do not allow duplicate values, list of clients on the server

async def handler(websocket):
    # Register
    clients.add(websocket)
    print("There are", len(clients), "clients on the server")
    try:
        async for message in websocket:
            print(message)
            print(websocket.remote_address) # ip and port
            # broadcast to everyone else:
        for client in clients:
            if client != websocket:
                await client.send(message)
    except websockets.ConnectionClosed:
        class classname():
            pass
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "127.0.0.1", 8765): # localhost
        print("Websocket server online")
        await asyncio.Future() #run forever

if __name__ == "__main__":
    asyncio.run(main())
