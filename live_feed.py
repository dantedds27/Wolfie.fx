

import asyncio
import websockets

async def live_feed():
    print("Starting live feed...")
    url = "wss://ws.finnhub.io?token=demo"  # Replace 'demo' with your actual API token
    async with websockets.connect(url) as websocket:
       await websocket.send('{"type":"subscribe","symbol":"AAPL"}')
       async for message in websocket:
        print(f"Received message: {message}")

asyncio.run(live_feed())
