# File: Short.py

# words.txt stores words that are of length 3-6
file_short = open('../textfiles/words.txt', 'r')

# Global
short_array = []

# Adds all to a list
def add_all(file):
    list = []
    for line in file:
        list.append(line.rstrip())
    return list

# Length: 260
short_array = add_all(file_short)

# Close
file_short.close()