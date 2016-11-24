# File: Long.py
import random

# CROSSWD.TXT stores words that are length of 7
file_long = open('../textfiles/CROSSWD.TXT', 'r')

# Global
seven = [] # Length: 21727
store = [] # Length: 92082

# Splits Strings into two arrays
def add_and_strip(file):
    list = []
    other_list = []
    for line in file:
        if len(line) is 9:
            list.append(line.rstrip())
        elif len(line) >= 5 or len(line) < 9:
            other_list.append(line.rstrip())

    global store, seven
    store = other_list
    seven = list

# Call
add_and_strip(file_long)

# Close
file_long.close()