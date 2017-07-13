#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <stdlib.h>


class WordScramble {
private:
  std::map<std::string, int> extract(std::ifstream inputFile);  // creates a map using the words keys and lengths as values
  std::string selectRandomWord(const std::map<std::string, int>& map);  // selects a random word from the map
  std::string scrambleWord(const std::string& word);  // scrambles word
  std::map<std::string, std::vector<int>> analyze(const std::string& word);  // records number of letter occurrances for each word
  bool operator==(const std::string& word);  // checks if the number of letters in a word is valid to use
  std::map<std::string, int> match(std::string chosenWord,
				   const std::map<std::string, std::vector<int>>& wordBank,
				   int length
				   );
  WordScramble();  // removes default constructor


public:
    WordScramble(std::ifstream inputFile);
    ~WordScramble();
}
