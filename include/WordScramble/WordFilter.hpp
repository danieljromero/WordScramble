#ifndef WORDSCRAMBLE_WORDFILTER_HPP
#define WORDSCRAMBLE_WORDFILTER_HPP

#include <fstream>
#include <iostream>
#include <vector>


class WordFilter {
public:
    WordFilter(const std::string &inputFile, const unsigned int &difficulty);

    ~WordFilter();

    void showStats();

private:
    std::vector<unsigned int> stats;

    void setStats(const unsigned int &size);

    void process(const std::string &file, const unsigned int &range);
};

#endif //WORDSCRAMBLE_WORDFILTER_HPP
