cmake_minimum_required (VERSION 3.16.3)
project (TCP_Server)

set (CMAKE_BUILD_TYPE DEBUG)
set (CXX_STANDARD 17)
add_compile_options (-std=c++17 -Wall -Werror=switch -O3 -ggdb)

set (INCLUDE_DIRS
  include
)

set (SOURCES
  src/main_TCP_Server.cpp
  src/TCP_Server.cpp
)

add_executable (${PROJECT_NAME} ${SOURCES})

target_include_directories (${PROJECT_NAME} PRIVATE ${INCLUDE_DIRS})
