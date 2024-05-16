import asyncio
import websockets

async def server(websocket, path):
    while True:
        try:
            message = await websocket.recv()
        
            await websocket.send(f"已收到來自Client的訊息: {message}")
        except websockets.exceptions.ConnectionClosedOK:
            print("Client disconnected")
            break

async def main():
    async with websockets.serve(server, "127.0.0.1", 8080):
        print('start server: 127.0.0.1:8080')
        await asyncio.Future()  # run forever

if __name__=='__main__':
    asyncio.run(main())