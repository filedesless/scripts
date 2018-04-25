cmake_minimum_required (VERSION 2.6)
project(some_project_name)

set (CMAKE_CXX_STANDARD 11)

add_executable (some_executable_name some_source_file.cpp)
target_link_libraries (some_executable_name some_library)
