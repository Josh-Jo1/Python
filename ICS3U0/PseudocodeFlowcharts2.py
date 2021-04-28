#pseudocode & flowcharts 2
#Joshua Johnson
#March 5, 2018

passes = failures = 0
student = 1

while student <= 10:
    examresult = int(input("Enter the numerical exam result: "))
    if examresult >= 50:
        passes += 1
    else:
        failures += 1
    student += 1

print("\nPasses: ", passes)
print("Failures: ", failures)
if passes >= 8:
    print("\nRaise tuition")

