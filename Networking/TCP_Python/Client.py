# project imports
from Common import HOST, PORT

# python imports
import socket
import sys

# Open the socket as a context manager to avoid the need to explicitly invoke sock.close().
# AF_INET is the Internet address family for IPv4.
# SOCK_STREAM is the socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

  # Connect to the server
  sock.connect((HOST, PORT))

  # Send bytes of data to the server
  sock.sendall(b'Hello, world!')

  # Read the server's reply (up to 1024 bytes of data)
  data = sock.recv(1024)

print(f'Received {sys.getsizeof(data)} bytes of data from the server: {data}')

