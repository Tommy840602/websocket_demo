import asyncio
import websockets

async def client():
    async with websockets.connect("ws://127.0.0.1:8080") as websocket:
        while True:
            message = input("請輸入訊息 (type 'exit' to quit): ")
            await websocket.send(message)

            if message.lower() == "exit":
                break

            response = await websocket.recv()
            print(f"來自Server的訊息: {response}")


if __name__=='__main__':
    asyncio.run(client())