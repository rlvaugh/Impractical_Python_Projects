"""Find all the anagrams in a dictionary file for a given word.

Requires access to an external English word dictionary file
and file-loading module "load_dictionary.py"

"""

import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

anagram_list = []

# input a SINGLE word or SINGLE name below to find its anagram(s):
name = 'Foster'
print("Input name = {}".format(name))
name = name.lower()
print("Using name = {}".format(name))

# sort name and find anagrams
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:        
            anagram_list.append(word)

#print out list of anagrams
print()
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name!")
else:
    print("Anagrams =", *anagram_list, sep='\n')
