import socket

# Resolve local host to an IP address
HOST = socket.gethostbyname('localhost') # "127.0.0.1"

# Port numbers under 1024 require special privileges.
# Therefore, use any port number above 1024.
# Port 8080 is a conventional port number
PORT = 8080


