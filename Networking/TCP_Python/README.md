# TCP Example in Python
## Description
The server awaits data from the client. Once data is received from the client, the server sends a reply back to the client.

## Usage
1. Run `Server.py` in a terminal.
1. Then, run `Client.py` in a different terminal.

## Expected Output
Server:
```
Server is attempting to bind to 127.0.0.1:8080.
Server is binded to 127.0.0.1:8080.
Server is awaiting a connection with the client on 127.0.0.1:8080...
Server is connected to the client on 127.0.0.1:54219.
Server received 46 bytes of data from the client: Hello, world!
Server echoed the received data back to the client.
```

Client:
```
Client is attempting a connection to the server at 127.0.0.1:8080.
Client is connected to 127.0.0.1:8080.
Client is sending data to the server: Hello, world!
Client is awaiting a response from the server.
Client received 46 bytes of data from the server: Hello, world!
```

## Codebase Explained
`Common.py` is a module that contains IP address and port configurations used by both the `Client.py` and `Server.py` modules.
