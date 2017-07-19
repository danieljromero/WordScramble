cmake_minimum_required(VERSION 3.7)
project(WordScramble)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-g3 -Wall -Wno-sign-compare -Werror -Wno-unused-variable -std=c++11")

set(SOURCE_FILES src/main.cpp src/WordFilter.hpp src/WordFilter.cpp)
add_executable(WordScramble ${SOURCE_FILES})