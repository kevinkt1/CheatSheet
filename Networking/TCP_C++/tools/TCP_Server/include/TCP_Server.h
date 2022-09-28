#ifndef TCP_SERVER_H
#define TCP_SERVER_H

// stl includes
#include <string>

class TCP_Server
{
public:
  TCP_Server(const std::string& ipAddress, unsigned short port);

  ~TCP_Server();

private:
  /**
   * @note https://www.gnu.org/software/libc/manual/html_node/Local-Socket-Example.html
   */
  int makeNamedSocket(const char* filename);
};

#endif
