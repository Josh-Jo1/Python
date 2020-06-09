# Problem D
# Given a non-negative integer, remove k digits from the number so that the new number is the smallest possible.

myInput = "Y"
dataFile = open("Problem D data.txt")       # or use path of text file

while(myInput.upper() == "Y"):
    # line format: integer + " " + k + " " + answer
    # example: 560943 3 43
    line = dataFile.readline()

    if line == "End":
        print("Data completed")
        break

    integer = line[:line.find(" ")]
    n = line[line.find(" ") + 1]                        # if k is one digit
    answer = 0
    
    for i in range(2, len(line) - line.find(" ")):      # if k is more than one digits
        if line[line.find(" ") + i] != " ":
            n += line[line.find(" ") + i]
        else:
            answer = int(line[line.find(" ") + i:])
            break

    digits = [int(i) for i in integer]
    k = int(n)

    # used while loops instead of for loops for ability to restart loop from beginning

    # zeroes at beginning are advantageous since removing numbers prior to them also removes leading 0
    # example: 23062349, k = 2 would make smallest new number 62349
    i = 0
    while i < k and i < len(digits):
        if digits[i] == 0:
            k -= len(digits[:i])
            digits = digits[i + 1:]
            i = -1
        if len(digits) == 0: break
        i += 1

    # next, remove numbers followed by smaller numbers
    # example: 62394, k = 2 would make smallest new number 234
    i = 0
    while i < len(digits) - 1 and k != 0:
        if digits[i] > digits[i + 1]:
            k -= 1
            del digits[i]
            i = -1
        i += 1

    # lastly, remove largest numbers
    # example: 234, k = 1 would make smallest new number 23
    for i in range(k):
        if len(digits) > 0:
            k -= 1
            digits.remove(max(digits))

    result = "0"                                                # in case full number is deleted
    for i in range(len(digits)): result += str(digits[i])
    print(int(result))

    if int(result) == answer: print("True")
    else: print("False")

    myInput = input("Next line? Y/N: ")

dataFile.close()
