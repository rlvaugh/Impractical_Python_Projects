"""Map letters from string into dictionary & print bar chart of frequency."""
import sys
import pprint
from collections import defaultdict

# Note: text should be a short phrase for bars to fit in Idel window
random_text = 'Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same.'

random_letters = 'abcdefghijklmnopqrstuvwxyz'

# defaultdict module lets you build dictionary keys on the fly!
mapped = defaultdict(list)
for character in random_text:
    new_character = character.lower()
    if character in random_letters:
        mapped[new_character].append(character)

# pprint lets you to print the stacked output of this program
print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text = ", end='')
print("{}\n".format(text), file=sys.stderr)
pprint.pprint(mapped, width=110)
