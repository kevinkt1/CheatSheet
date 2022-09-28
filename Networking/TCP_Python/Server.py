# project imports
from Common import HOST, PORT

# python imports
import socket
import sys

# Open the socket as a context manager to avoid the need to explicitly invoke sock.close().
# AF_INET is the Internet address family for IPv4.
# SOCK_STREAM is the socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

  # The address family of the socket dictates the values to be passed into the sock.bind() invocation
  print(f'Server is attempting to bind to {HOST}:{PORT}.')
  sock.bind((HOST, PORT))
  print(f'Server is binded to {HOST}:{PORT}.')

  # Enable the server to accept connections.
  # This method accepts a 'backlog' integer parameter, which is defaulted to a reasonable value.
  # Increase the backlog value to handle higher numbers of simultaneous connection requests
  sock.listen()

  print(f'Server is awaiting a connection with the client on {HOST}:{PORT}...')

  # This method blocks until a client connects.
  # 'conn' is a new socket object for communicating with the client.
  # 'conn' is distinct from the listening socket that the server is using to accept new connections.
  # 'addr' is a tuple containing the IP address string and the port integer
  conn, addr = sock.accept()

  # Again, take advantage of the context manager to avoid the need to explicitly invoke conn.close()
  with conn:
    print(f'Server is connected to the client on {addr[0]}:{addr[1]}.')

    # Receive up to 1024 bytes of data from the client
    dataBytes = conn.recv(1024)
    
    print(f'Server received {sys.getsizeof(dataBytes)} bytes of data from the client: {dataBytes.decode()}')

    # Echo the received data back to the client
    conn.sendall(dataBytes)
    print('Server echoed the received data back to the client.')

