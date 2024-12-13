
import asyncio  # Import asyncio for handling asynchronous tasks
import websockets  # Import websockets library to create WebSocket servers and clients


"""
How to Test

This setup demonstrates the basics of sending and receiving messages over a WebSocket connection.
This code can be run locally on your laptop.

- Start the WebSocket server by running the Python script (websocket_server.py) from the terminal (Terminal: 
$ python websocket_server.py)
- Double click the HTML file (websocket_client.html) to open it in a web browser.
- Type a message in the input box and click "Send." 
- The server will echo the message back, and you'll see it displayed in the browser.

"""



# Define an asynchronous function to handle WebSocket connections
async def echo(websocket, path):
    """
    Handles a single WebSocket connection.

    Args:
        websocket: The WebSocket connection object.
        path: The URL path of the connection (not used here).
    """
    # Listen for messages from the client
    async for message in websocket:
        print(f"Received message: {message}")  # Print the received message to the server console
        
        # Send a response back to the client
        await websocket.send(f"Echo: {message}")  # Echo the received message with a prefix "Echo:"
		
		
		

# Define the main function to start the WebSocket server
async def main():
    """
    Sets up and runs the WebSocket server.
    """
    # Start a WebSocket server that listens on localhost at port 6789
    async with websockets.serve(echo, "localhost", 6789):
        print("WebSocket server is running on ws://localhost:6789")
        
        # Keep the server running indefinitely
        await asyncio.Future()  # A dummy future object that never resolves
		
		

# Entry point for the script
if __name__ == "__main__":
    # Run the main function inside an asyncio event loop
    asyncio.run(main())
	
	
	