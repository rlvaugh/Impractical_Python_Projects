"""Remove single-letter words from list if not 'a' or 'i'."""
word_list = ['a', 'nurses', 'i', 'stack', 'b', 'c', 'cat']
word_list_clean = []

permissible = ('a', 'i')

# remove single-letter words if not "a" or "I"
for word in word_list:
    if len(word) > 1:
        word_list_clean.append(word)
    elif len(word) == 1 and word in permissible:
        word_list_clean.append(word)
    else:
        continue

print("{}".format(word_list_clean))
