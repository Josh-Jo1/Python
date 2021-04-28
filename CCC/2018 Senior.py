# Make separate files for submission then move code here

# Call
Problem1()


def Problem1():
    numberOfVillages = int(input())

    villages = []

    for i in range(numberOfVillages):
        villages.append(int(input()))

    villages.sort()

    neighbourhoodLimit = []

    for i in range(numberOfVillages - 1):
        neighbourhoodLimit.append((villages[i] + villages[i + 1]) / float(2))

    smallest = neighbourhoodLimit[1] - neighbourhoodLimit[0]

    for i in range(numberOfVillages - 3):
        if neighbourhoodLimit[i + 2] - neighbourhoodLimit[i + 1] < smallest:
            smallest = neighbourhoodLimit[i + 2] - neighbourhoodLimit[i + 1]

    print(smallest)

#Little more work from Junior Problem 4, still incomplete
def Problem2():
    inputRows = int(input())
    flowers = []

    # Better way of making list from string
    for i in range(inputRows):
        x = input().split()
        flowers.append(x)

    # Rotate
    rotate = True
    while (rotate == True):
        rotate = False
        
        for i in range(inputRows - 1):
            if flowers[i][0] > flowers[i + 1][0]:
                flowers = list(zip(*flowers[::-1]))
                rotate = True
                break
            else:
                for j in range(inputRows - 1):
                    if flowers[i][j] > flowers[i][j + 1]:
                        flowers = list(zip(*flowers[::-1]))
                        rotate = True
                        break

    for flower in flowers:
        print(" ".join(flower))

