cmake_minimum_required(VERSION 3.8)
project(clump)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        clump.cc)

add_executable(clump ${SOURCE_FILES})
