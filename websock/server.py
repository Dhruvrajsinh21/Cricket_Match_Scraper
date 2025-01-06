import asyncio
import websockets

connected_clients = set()

# WebSocket connection handler
async def websocket_handler(websocket):
    """Handles WebSocket connections and disconnections."""
    connected_clients.add(websocket)
    print(f"New client connected. Total clients: {len(connected_clients)}")

    try:
        async for message in websocket:
            print(f"Received message: {message}")
            await notify_clients(message)
    except websockets.ConnectionClosed as e:
        print(f"Client disconnected unexpectedly: {e}")
    finally:
        connected_clients.remove(websocket)
        print(f"Client disconnected. Total clients: {len(connected_clients)}")

# Notify all connected clients
async def notify_clients(data):
    """Sends data to all connected clients."""
    if connected_clients:
        tasks = []
        for client in connected_clients:
            try:
                tasks.append(client.send(data))
            except (websockets.exceptions.ConnectionClosed, Exception) as e:
                print(f"Error sending data to client: {e}")
                connected_clients.discard(client)
    
        if tasks:
            await asyncio.gather(*tasks)

# Start WebSocket server
async def start_websocket_server():
    """Starts the WebSocket server."""
    server = await websockets.serve(websocket_handler, "localhost", 6789)
    print("WebSocket server started at ws://localhost:6789")
    await server.wait_closed()

# Run the server
def run_server():
    """Runs the WebSocket server."""
    asyncio.run(start_websocket_server())

if __name__ == "__main__":
    run_server()
