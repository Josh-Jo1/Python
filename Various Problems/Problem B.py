# Problem B
# Efficiently calculate the sum of the Fibonacci sequence from term 1 (zero) up to and including a given term.
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# Sum of sequence: 0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143

# Input an integer to find sum till that term. Input a letter to end program.
inputTerm = input()

# Method 1

# while inputTerm.isnumeric():
#     inputTerm = int(inputTerm)

#     if inputTerm < 1: print("Invalid term")
#     elif inputTerm <= 3: print("Sum:", inputTerm - 1)
#     else:
#         number1 = number2 = 1
#         sumOfSequence = 2
#         i = 3
#         for i in range(3, inputTerm):
#             nextNumber = number1 + number2
#             sumOfSequence += nextNumber
#             number1 = number2
#             number2 = nextNumber
#         print("Sum:", sumOfSequence)

#     inputTerm = input()

########################################################################################################################

# Method 2

# def FibonacciNumber(term):
#     if term == 2 or term == 3: return 1

#     return FibonacciNumber(term - 1) + FibonacciNumber(term - 2)

# while inputTerm.isnumeric():
#     inputTerm = int(inputTerm)

#     if inputTerm < 1: print("Invalid term")
#     elif inputTerm <= 3: print("Sum:", inputTerm - 1)
#     else:
#         sumOfSequence = 2
#         for i in range(4, inputTerm + 1): sumOfSequence += FibonacciNumber(i)
#         print("Sum:", sumOfSequence)
    
#     inputTerm = input()

########################################################################################################################

# Method 3
# This method is a significant improvement from the last since it saves time by applying memoization.

# sequence = {1:0, 2:1, 3:1}

# def FibonacciNumber(term):
#     if term in sequence: return sequence[term]
#     else:
#         sequence[term] = FibonacciNumber(term - 1) + FibonacciNumber(term - 2)
#         return sequence[term]

# while inputTerm.isnumeric():
#     inputTerm = int(inputTerm)

#     if inputTerm < 1: print("Invalid term")
#     elif inputTerm <= 3: print("Sum:", inputTerm - 1)
#     else:
#         sumOfSequence = 2
#         for i in range(4, inputTerm + 1): sumOfSequence += FibonacciNumber(i)
#         print("Sum:", sumOfSequence)

#     inputTerm = input()

########################################################################################################################

# Method 4
# Some research lead me to find a formula to calculate the n-th term of the Fibonacci Sequence:
# F(n) = [(Phi)^n – (phi)^n] / Sqrt[5], where Phi = (1 + Sqrt[5]) / 2 and phi = (1 – Sqrt[5]) / 2.
# Note: If n = 5, F(n) = 5, but I want F(n) = 3 based on term number so I adapted to n = n - 1.

# import math

# def FibonacciNumber(term):
#     Phi = (1 + math.sqrt(5)) / 2
#     phi = (1 - math.sqrt(5)) / 2

#     return (pow(Phi, term - 1) - pow(phi, term - 1)) / math.sqrt(5)

# while inputTerm.isnumeric():
#     inputTerm = int(inputTerm)

#     if inputTerm < 1: print("Invalid term")
#     elif inputTerm <= 3: print("Sum:", inputTerm - 1)
#     else:
#         sumOfSequence = 2
#         for i in range(4, inputTerm + 1): sumOfSequence += int(FibonacciNumber(i))
#         print("Sum:", sumOfSequence)

#     inputTerm = input()

########################################################################################################################

# Method 5
# After further research, I found out the sum till F(n) = F(n+2) - F(2)

import math

def FibonacciNumber(term):
    Phi = (1 + math.sqrt(5)) / 2
    phi = (1 - math.sqrt(5)) / 2

    return (pow(Phi, term - 1) - pow(phi, term - 1)) / math.sqrt(5)

while inputTerm.isnumeric():
    inputTerm = int(inputTerm)

    if inputTerm < 1: print("Invalid term")
    elif inputTerm <= 3: print("Sum:", inputTerm - 1)
    else:
        print("Sum:", int(FibonacciNumber(inputTerm + 2) - 1))

    inputTerm = input()
