# Importing the relevant libraries
import websockets
import asyncio
# Server data
PORT = 7890
print("Server listening on Port " + str(PORT))


# The main behavior function for this server
async def echo(websocket, path):
    print("A client just connected")

# Start the server
start_server = websockets.serve(echo, "localhost", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()