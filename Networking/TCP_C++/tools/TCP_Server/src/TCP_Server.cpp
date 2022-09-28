#include "TCP_Server.h"

// gnu c libaries
#include <stddef.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/un.h>

TCP_Server::TCP_Server(const std::string& ipAddress, unsigned short port)
{
  int
}

TCP_Server::~TCP_Server()
{
}

int TCP_Server::makeNamedSocket(const char *filename)
{
  struct sockaddr_un name;
  int sock;
  size_t size;

  /* Create the socket. */
  sock = socket(PF_LOCAL, SOCK_STREAM, 0);
  if (sock < 0)
  {
    perror("socket");
    exit(EXIT_FAILURE);
  }

  /* Bind a name to the socket. */
  name.sun_family = AF_LOCAL;
  strncpy(name.sun_path, filename, sizeof(name.sun_path));
  name.sun_path[sizeof(name.sun_path) - 1] = '\0';

  /* The size of the address is
     the offset of the start of the filename,
     plus its length (not including the terminating null byte).
     Alternatively you can just do:
     size = SUN_LEN (&name);
 */
  size = (offsetof (struct sockaddr_un, sun_path)
          + strlen (name.sun_path));

  if (bind(sock, (struct sockaddr *) &name, size) < 0)
  {
    perror("bind");
    exit(EXIT_FAILURE);
  }

  return sock;
}
