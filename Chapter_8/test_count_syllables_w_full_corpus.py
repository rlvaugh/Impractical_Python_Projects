"""Check syllable-counting program against training corpus for haiku."""
import sys
import count_syllables

with open('train.txt.') as in_file:
    words = set(in_file.read().split())

missing = []

for word in words:
    try:
        num_syllables = count_syllables.count_syllables(word)
##        print(word, num_syllables, end='\n') # uncomment to see word counts
    except KeyError:
        missing.append(word)

print("Missing words:", missing, file=sys.stderr)
