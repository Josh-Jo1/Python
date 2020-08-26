# Challenge: Write a Python function to find all prime factors.
# Input: integer value; Output: list of prime factors

integer = int(input())
factor = 2
primeFactors = []

while (factor <= integer):
    if (integer % factor == 0):
        primeFactors.append(factor)
        integer = integer/factor
    else:
        factor += 1

print(primeFactors)
