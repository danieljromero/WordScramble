#include "../include/WordScramble/WordFilter.hpp"


WordFilter::WordFilter(const std::string &inputFile, const unsigned int &difficulty) {
    this->setStats(difficulty);
    this->process(inputFile, difficulty);
}

WordFilter::~WordFilter() {
    this->stats.clear();
}

void WordFilter::setStats(const unsigned int &size) {
    this->stats.reserve(size);
    for (unsigned int i = 0; i < size; ++i) {
        this->stats.push_back(0);
    }
}

void WordFilter::showStats() {
    for (std::vector<unsigned int>::const_iterator i = this->stats.begin(); i != this->stats.end(); ++i) {
        std::cout << *i << std::endl;
    }
}

void WordFilter::process(const std::string &file, const unsigned int &range) {

    std::ifstream inputStream;
    inputStream.exceptions(std::ifstream::badbit);

    try {
        inputStream.open(file, std::ios::in);
    } catch (const std::ifstream::failure &err) {
        std::cerr << "Exception during open." << std::endl;
        exit(EXIT_FAILURE);
    }

    try {
        std::string line;
        while (std::getline(inputStream, line)) {
            line.erase(line.size() - 1);
            if (line.size() <= range) {
                this->stats.at(line.size() - 1) += 1;
            }
        }
    } catch (std::ios_base::failure &err) {
        std::cerr << " Exception during read." << std::endl;
        exit(EXIT_FAILURE);
    }

    if (inputStream.is_open()) inputStream.close();
}
