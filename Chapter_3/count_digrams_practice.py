"""Generate letter pairs in Voldemort & find their frequency in a dictionary.

Requires load_dictionary.py module to load an English dictionary file.

"""
import re
from collections import defaultdict
from itertools import permutations
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

name = 'Voldemort'  #(tmvoordle)
name = name.lower()

# generate unique letter pairs from name
digrams = sorted([''.join(i) for i in permutations(name, 2)])
print(*digrams, sep='\n')
print("\nNumber of digrams = {}\n".format(len(digrams)))

# use regular expressions to find repeating digrams in a word
mapped = defaultdict(int)
for word in word_list:
    word = word.lower()
    for digram in digrams:
        for m in re.finditer(digram, word):
            mapped[digram] += 1

print("Digram frequency count:")
keys = sorted(mapped.keys())
for k in keys:
    print("{} {}".format(k, mapped[k]))
