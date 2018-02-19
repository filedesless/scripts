cmake_minimum_required(VERSION 3.1)
project(solution)

include_directories(/usr/local/opt/openssl/include)
link_directories(/usr/local/opt/openssl/lib)

add_executable(solution private-from-pq.c)

target_link_libraries(solution crypto)
