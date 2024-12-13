import asyncio
import websockets


"""
How to Test

This setup demonstrates the basics of sending and receiving messages over a WebSocket connection.
This code can be run locally on your laptop.

- Start the WebSocket server by running the Python script (websockets_server_multiple-clients.py) from the terminal (Terminal: 
$ python websockets_server_multiple-clients.py)
- Double click the HTML file (websockets-multiple-clients.html) to open it in a web browser (open three tabs).
- Type a message in the input box and click "Send." 
- You will see the message displayed in all the tabs you have opened.

"""

# List to keep track of connected clients
connected_clients = set()

async def handle_client(websocket, path):
    # Add the new client to the connected clients set
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Message received: {message}")
            # Broadcast the message to all connected clients
            for client in connected_clients:
                await client.send(message)
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")
    finally:
        # Remove the client from the connected clients set when disconnected
        connected_clients.remove(websocket)

# Start the WebSocket server
start_server = websockets.serve(handle_client, "localhost", 6789)

print("WebSocket server is running on ws://localhost:6789")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
