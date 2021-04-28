# Challenge: Write a Python function to determine the probability of certain outcomes when rolling dice.
# Must use Monte Carlo Method - 1,000,000 simulations
# Input: variable number of arguments for sides of dice;   Output: table of probability for each possible outcome


# While coding this function, the main problem I faced was runtime. The provided solution seemed to work very quickly in the video,
# which left me confused about what I was doing wrong. Using 
from time import time
# I compared the runtime of my solution to the provided solution. Both output tables matched. The results are as follows:
# (Note that the times below are the average of 2 consecutive runs)

# My Solution
# probability(4,6,6) ran in 2.79 seconds for 100,000 simulations
# probability(4,6,6) ran in 26.23 seconds for 1,000,000 simulations

# Provided Solution
# roll_dice(4,6,6) ran in 5.79 seconds for 100,000 simulations
# roll_dice(4,6,6) ran in 55.56 seconds for 1,000,000 simulations



# My Solution

from random import randint

def probability(dice):
    SIMS = 1000000
    occurrences = {}

    for i in range(SIMS):
        roll = 0
        for sides in dice:
            roll += randint(1,sides)

        if roll in occurrences:
            occurrences[roll] += 1
        else:
            occurrences[roll] = 1
    
    print("\nOUTCOME  PROBABILITY")
    for outcome in sorted(occurrences):
        print("{}  {}%".format(outcome, round(occurrences[outcome]/SIMS*100, 2)))

dice = [int(n) for n in input().split(',')]
# dice = [int(n) for n in "4,6,6".split(',')]

start = time()

probability(dice)

print(time() - start)



# Provided Solution - made note for comparison

# from random import randint
# from collections import Counter

# def roll_dice(*dice, num_trials=1_000_000):
#     counts  = Counter()
#     for roll in range(num_trials):
#         counts[sum((randint(1,sides) for sides in dice))] += 1

#     print('\nOUTCOME\tPROBABILITY')
#     for outcome in range(len(dice), sum(dice)+1):
#         print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/num_trials))

# start = time()

# roll_dice(4,6,6)

# print(time() - start)
