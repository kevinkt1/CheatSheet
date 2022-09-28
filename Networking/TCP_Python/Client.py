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
  print(f'Client is attempting a connection to the server at {HOST}:{PORT}.')
  sock.connect((HOST, PORT))
  print(f'Client is connected to {HOST}:{PORT}.')

  # Send bytes of data to the server
  dataStr = 'Hello, world!'
  print(f'Client is sending data to the server: {dataStr}')
  sock.sendall(dataStr.encode())

  # Read the server's reply (up to 1024 bytes of data)
  print(f'Client is awaiting a response from the server.')
  dataBytes = sock.recv(1024)

  print(f'Client received {sys.getsizeof(dataBytes)} bytes of data from the server: {dataBytes.decode()}')

