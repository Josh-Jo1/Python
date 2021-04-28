# Make separate files for submission then move code here

# Call
Problem1()


def Problem1():
    season = int(input())

    swifts = input().split()
    semaphores = input().split()

    sameRuns = 0
    swiftsRuns = int(swifts[0])
    semaphoresRuns = int(semaphores[0])

    for i in range(season - 1):
        if swiftsRuns == semaphoresRuns:
            sameRuns = i + 1
        
        swiftsRuns += int(swifts[i + 1])
        semaphoresRuns += int(semaphores[i + 1])

    if swiftsRuns == semaphoresRuns:
        print(season)
    else:
        print(sameRuns)

def Problem2():
    measurements =  int(input())
    tides = input().split()

    tides = list(map(int, tides))

    ordered = []

    for i in range(measurements):
        if i % 2 == 0:
            ordered.append(max(tides))
            tides.remove(max(tides))
        else:
            ordered.append(min(tides))
            tides.remove(min(tides))

    ordered.reverse()
    ordered = list(map(str, ordered))

    print(" ".join(ordered))