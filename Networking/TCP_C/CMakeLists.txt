cmake_minimum_required (VERSION 3.16.3)
project (TCP C)

set (CMAKE_BUILD_TYPE DEBUG)

# Build TCP Client
set (TCP_CLIENT_SOURCES
	main_TCP_Client.c
)

add_executable (TCP_Client ${TCP_CLIENT_SOURCES})

# Build TCP Server
set (TCP_SERVER_SOURCES
	main_TCP_Server.c
)

add_executable (TCP_Server ${TCP_SERVER_SOURCES})

