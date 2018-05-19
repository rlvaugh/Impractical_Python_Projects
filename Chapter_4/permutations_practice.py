"""For a total number of columns, find all unique column arrangements.

Builds a list of lists containing all possible unique arrangements of
individual column numbers including negative values for route direction
(read up column vs. down).

Input:
-total number of columns

Returns:
-list of lists of unique column orders including negative values for
route cipher encryption direction

"""
import math
from itertools import permutations, product

#------BEGIN INPUT-----------------------------------------------------------

# Input total number of columns:
num_cols = 4

#------DO NOT EDIT BELOW THIS LINE--------------------------------------------




# generate listing of individual column numbers
columns = [x for x in range(1, num_cols+1)]
print("columns = {}".format(columns))

# build list of lists of column number combinations
# itertools product computes the cartesian product of input iterables 
def perms(columns):
    """Take number of columns integer & generate pos & neg permutations."""
    results = []
    for perm in permutations(columns):
        for signs in product([-1, 1], repeat=len(columns)):
            results.append([i*sign for i, sign in zip(perm, signs)])
    return results

col_combos = perms(columns)
print(*col_combos, sep="\n")  # comment-out for num_cols > 4!
print("Factorial of num_cols without negatives = {}"
      .format(math.factorial(num_cols)))
print("Number of column combinations = {}".format(len(col_combos)))
