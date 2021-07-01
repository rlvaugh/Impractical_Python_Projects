"""Generate letter pairs & find their frequency in dictionary file.

Requires load_dictionary.py module to load an English dictionary file.

"""

import re
from collections import defaultdict
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt', 'r')

name = 'voldemort'

# generate unique letter pairs from name
digrams = set()
for letter in name:
    for i in range(0, len(name)):
        pair = letter + name[i]
        digrams.add(pair)
print(*sorted(digrams), sep='\n')
print()
print("Number of digrams = {}".format(len(digrams)))
print()

# use regular expressions to find repeating digrams in a word
# mark each occurrence of digrams with dictionary value = 'x'
# count number of 'x' per digram
mapped = defaultdict(list)
for word in word_list:
    for digram in digrams:
        for m in re.finditer(digram, word):
            mapped[digram].append('x')

print("digram frequency count:")
count = 0
for k in sorted(mapped):
    print("{} {}".format(k, len(mapped[k])))

