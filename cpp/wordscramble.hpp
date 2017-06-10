#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <stdlib.h>


class WordScramble {
private:
    std::map<std::string, int> extract(std::ifstream inputFile);
    std::string selectRandomWord(const std::map<std::string, int>& map);
    std::string scrambleWord(const std::string& word);
    std::map<std::string, std::vector<int>> analyze(const std::string& word);
    bool operator==(const std::string& word);
    std::map<std::string, int> match(
      std::string chosenWord,
      const std::map<std::string, std::vector<int>>& wordBank,
      int length);
    WordScramble();


public:
    WordScramble(std::ifstream inputFile);
    ~WordScramble();
}
