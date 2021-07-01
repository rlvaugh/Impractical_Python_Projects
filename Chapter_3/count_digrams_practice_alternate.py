"""Generate letter pairs & find their frequency in dictionary file.

Requires load_dictionary.py module to load an English dictionary file.
Includes contributions by Cliff McCullough.

"""

import re
from collections import defaultdict
from itertools import permutations
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt', 'r')
name = 'voldemort'

# generate unique letter pairs from name
digrams = set()
perms = {''.join(i) for i in permutations(name)}
for perm in perms:
    for i in range(0, len(perm) - 1):
        digrams.add(perm[i] + perm[i + 1])
print(*sorted(digrams), sep='\n')
print()
print("Number of digrams = {}".format(len(digrams)))
print()

# use regular expressions to find repeating digrams in a word
mapped = defaultdict(int)
for word in word_list:
    for digram in digrams:
        for m in re.finditer(digram, word):
            mapped[digram] += 1

print("Digram frequency count:")
count = 0
for k in mapped:
    keys = sorted(mapped.keys())
for k in keys:    
    print("{} {}".format(k, mapped[k]))
