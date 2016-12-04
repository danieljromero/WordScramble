# File: Combinations.py
from Scramble import _retVal
from Short import short_array
#from Long import file_long

# Array list of Char
_charList = list(_retVal)

# Creates a list of ALL words that start with a letter from _retVal
def first_check(list):
    newList = set()
    i = 0
    global _retVal
    while (i < 7):
        for string in list:
            if _retVal[i] == string[0]:
                newList.add(string)
        i = i + 1
    if len(newList) < 1:
        return "no results found"
    return newList


results = list(sorted(first_check(short_array)))
results.sort(key=len, reverse=False)


print results
print len(results)
print len(results[0])

def second_check(list):
    global _charList
    wordSet = set()
    for string in list:
        i = 0
        j = len(string)

        set(string) & set(_charList)


        while (i != j):
            index = 0
            for letter in _charList:
                if string[i] == letter[index]:
                    wordSet.add(string)
                    index = index + 1
            i = i + 1
    return wordSet


r = second_check(results)
print r
print len(r)
