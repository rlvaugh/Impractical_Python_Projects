"""Use hill climbing to crack a lock combination."""
import time
from random import randint, randrange

def fitness(combo, attempt):
    """Compare items in two lists and count number of matches."""
    grade = 0
    for i, j in zip(combo, attempt):
        if i == j:
            grade += 1
    return grade

def main():
    """Enter lock combination & run hill climbing algorithm to find solution."""
    combination = '6822858902'
    print("Combination = {}".format(combination))
    # convert combination to list:
    combo = [int(i) for i in combination]

    # generate guess at combination & grade fitness:
    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0

    # evolve guess           
    while best_attempt != combo:
        # crossover
        next_try = best_attempt[:]
        # mutate
        lock_wheel = randrange(0, len(combo))
        next_try[lock_wheel] = randint(0, 9)
        # grade & select
        next_try_grade = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
        print(next_try, best_attempt)
        count += 1

    print()
    print("Cracked! {}".format(best_attempt), end=' ')
    print("in {} tries!".format(count))

if __name__ == '__main__':    
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was {:.5f} seconds.".format(duration))            
