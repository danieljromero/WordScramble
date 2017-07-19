#ifndef WORDSCRAMBLE_WORDFILTER_HPP
#define WORDSCRAMBLE_WORDFILTER_HPP

#include <fstream>
#include <iostream>


class WordFilter {
public:
    WordFilter(const std::string& inputFile);
    ~WordFilter();
};

#endif //WORDSCRAMBLE_WORDFILTER_HPP
