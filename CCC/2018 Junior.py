# Make separate files for submission then move code here

# Call
Problem1()


def Problem1():
    digit1 = int(input())
    digit2 = int(input())
    digit3 = int(input())
    digit4 = int(input())

    if (digit1 == 8 or digit1 == 9) and (digit2 == digit3) and (digit4 == 8 or digit4 == 9):
        print("ignore")
    else:
        print("answer")

def Problem2():
    numberOfParkingSpaces = int(input())
    spacesOccupiedYesterday = input()
    spacesOccuppiedToday = input()

    spacesOccuppiedBothDays = 0

    for i in range(0, numberOfParkingSpaces):
        if spacesOccupiedYesterday[i] == 'C' and spacesOccuppiedToday[i] == 'C':
            spacesOccuppiedBothDays += 1

    print(spacesOccuppiedBothDays)

def Problem3():
    distancesInput = input() + ' '

    # Create list of distances
    distances = []
    start = end = 0
    for i in range(0, 4):
        while distancesInput[end] != ' ':
            end += 1
        distances.append(int(distancesInput[start:end]))
        start = end = end + 1

    # Calculate first distances in list
    sum = 0
    firstDistances = [0]
    for i in range(0, 4):
        sum += distances[i]
        firstDistances.append(sum)
    print(" ".join(str(x) for x in firstDistances))

    # Calculate other distances
    sumOfDistances = 0
    for i in range(0, 4):
        sumOfDistances += distances[i]
        print(" ".join(str(abs(x - sumOfDistances)) for x in firstDistances))
    
# INCOMPLETE
def Problem4():
    inputRows = int(input())
    flowers = []

    # Better way of making list from string
    for i in range(inputRows):
        x = input().split()
        flowers.append(x)

    # Rotate
    flowers = list(zip(*flowers[::-1]))

    print(flowers)

