# TCP Example in C
## Description
The server awaits a connection from the client. Once the connection is established, the server sends a message to the client.

## Usage
1. Build this repository by creating a sibling directory to this folder. Suggest naming the folder `build`.
1. From that folder, run this command: `cmake -G "Eclipse CDT4 - Unix Makefiles" ../TCP_C++`
1. Next, run `make`.
1. Run the server executable by typing `./TCP_Server`.
1. Then, create another terminal window, and run the client executable by passing a hostname or IP address to the executable like such:
	* `./TCP_Client localhost`
	* `./TCP_Client 127.0.0.1`
1. Finally, stop the server by selecting the terminal running the server and hitting `CTRL + C`.

## Output
Server:
```
server: waiting for connections...
server: got connection from 127.0.0.1
```

Client:
```
client: connecting to 127.0.0.1
client: received 'Hello, world!'
```

