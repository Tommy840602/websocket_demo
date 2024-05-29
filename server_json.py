import asyncio
import websockets
import json

async def handle_message(websocket, path):
    async for message in websocket:
        try:
            # 解碼JSON訊息
            data = json.loads(message)
            print(f"Received message: {data}")

            # 在這裡進行你的處理邏輯，這裡只是簡單地回傳相同的訊息
            response_data = {"response": "Message received successfully!"}

            # 將回應編碼為JSON並發送回客戶端
            response_message = json.dumps(response_data)
            await websocket.send(response_message)

        except json.JSONDecodeError:
            print("Invalid JSON format")

async def main():
    async with websockets.serve(handle_message, "127.0.0.1", 8080):
        print('start server: 127.0.0.1:8080')
        await asyncio.Future()  # run forever

asyncio.run(main())
