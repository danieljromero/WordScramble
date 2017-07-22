
#include "../include/WordScramble/WordFilter.hpp"

int main() {
    WordFilter filter("src/dictionaries/small.txt", 5);
    filter.showStats();
    return 0;
}
