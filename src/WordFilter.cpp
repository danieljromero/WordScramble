#include "WordFilter.hpp"


WordFilter::WordFilter(const std::string& inputFile) {
    std::ifstream inputStream;
    inputStream.exceptions ( std::ifstream::failbit | std::ifstream::badbit );
    try {
        inputStream.open(inputFile, std::ios::in);
    } catch (const std::ifstream::failure& e) {
        std::cerr << "Unable to open/read/close file." << std::endl;
        exit(EXIT_FAILURE);
    }

}

WordFilter::~WordFilter() {

}
