#Problem 1
#15/15

sequence = input()

row1 = ['1','2']
row2 = ['3','4']

for i in range(len(sequence)):
    if sequence[i] == 'H':
        temp = row1
        row1 = row2
        row2 = temp
    else:
        temp = row1[0]
        row1[0] = row1[1]
        row1[1] = temp

        temp = row2[0]
        row2[0] = row2[1]
        row2[1] = temp

print(" ".join(row1))
print(" ".join(row2))

#Problem 2
#6/15 Time limit exceeded

cases = int(input())

integers = []

for i in range(cases):
    integers.append(int(input()))


def checkPrime(x):
    for i in range(2, int(x / 2) + 1):
        if x % i == 0:
            return False
    return True


for i in range(cases):
    if checkPrime(integers[i]):
        a = b = integers[i]
    else:
        x = 1
        a = integers[i] - x
        b = integers[i] + x

        primes = False
        while(primes == False):
            primes = True

            minimum = int(min(a, b) / 2) + 1
            for j in range(2, minimum):
                if (a % j == 0) or (b % j == 0):
                    primes = False
                    a -= 1
                    b += 1
                    break

    print(str(a) + " " + str(b))