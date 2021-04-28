# Problem A
# Given an array with numbers, write a program that efficiently determines the nearest larger value of the chosen index.

# To save time, add inputs here before running program.
inputArray = [1,8,9,1,7,3,2,8]
inputIndex = 0

# Method 1
# Finds distance to a larger value left and right of the chosen index, separately.
# Would be more efficient by checking left and right together and stop when larger value reached.

# def LeftShift(index, shifts):
#     while index - 1 >= 0:
#         shifts += 1
#         if inputArray[index - 1] > inputArray[inputIndex]:
#             return shifts
#         else:
#             index -= 1

#     return -1

# def RightShift(index, shifts):
#     while index + 1 <= len(inputArray) - 1:
#         shifts += 1
#         if inputArray[index + 1] > inputArray[inputIndex]:
#             return shifts
#         else:
#             index += 1
    
#     return -1

# if inputIndex >= 0 and inputIndex <= len(inputArray) - 1:
#     left = LeftShift(inputIndex, 0)
#     right = RightShift(inputIndex, 0)

#     if left == -1 and right == -1:
#         print("No larger value in array")
#     elif left == -1:
#         print(inputArray[inputIndex + right])
#     elif right == -1:
#         print(inputArray[inputIndex - left])
#     elif left < right:
#         print(inputArray[inputIndex - left])
#     elif left > right:
#         print(inputArray[inputIndex + right])
#     elif inputArray[inputIndex - left] > inputArray[inputIndex + right]:
#         print(inputArray[inputIndex - left])
#     else:
#         print(inputArray[inputIndex + right])
# else:
#     print("Chosen index not in array")

########################################################################################################################

# Method 2
# Finds distance left and right of chosen index simultaneously so that program will stop when larger value is found.

if inputIndex >= 0 and inputIndex <= len(inputArray) - 1:
    left = right = inputIndex
    
    while left >= 0 or right <= len(inputArray) - 1:
        left -= 1
        right += 1
        if left >= 0:
            if inputArray[left] > inputArray[inputIndex]: break
        if right <= len(inputArray) - 1:
            if inputArray[right] > inputArray[inputIndex]: break

    if left < 0 and right > len(inputArray) - 1:
        print("No larger value in array")
    elif left < 0:
        print(inputArray[right])
    elif right > len(inputArray) - 1:
        print(inputArray[left])
    elif inputArray[left] < inputArray[right]:
        print(inputArray[right])
    else:
        print(inputArray[left])
else:
    print("Chosen index not in array")