"""Use brute force to crack a lock combination."""
import time
from itertools import product

start_time = time.time()

combo = (9, 9, 7, 6, 5)

# use Cartesian product to generate permutations with repetition
for perm in product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=len(combo)):
    if perm == combo:
        print("Cracked! {} {}".format(combo, perm))

end_time = time.time()
print("\nRuntime for this program was {} seconds.".format
      (end_time - start_time))   
