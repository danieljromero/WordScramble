# File: Scramble.py
import random

from Long import _seven

# Random select
select = random.choice(_seven)

print "Original: " + select

# Length seven
prescramble = list(select)

# Shuffle String
random.shuffle(prescramble)

# Create New String
scramble = ''.join(prescramble)

print "Scrambled: " + scramble
print type(scramble)

# New String to List of Chars
_retVal = list(scramble)
