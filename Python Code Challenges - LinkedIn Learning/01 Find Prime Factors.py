# Challenge: Write a Python function to find all prime factors.
# Input: integer value;   Output: list of prime factors

def PrimeFactorization(intInput):
    factor = 2
    primeFactors = []

    while (factor <= intInput):
        if (intInput % factor == 0):
            primeFactors.append(factor)
            intInput = intInput/factor
        else:
            factor += 1

    return primeFactors

integer = int(input())

print(PrimeFactorization(integer))
