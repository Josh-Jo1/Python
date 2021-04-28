# Challenge: Write a Python function to determine if a given string is a palindrome.
# Input: string to evaluate;   Output: Boolean value
# Only consider letters (a-z), ignore case ('A' == 'a')

def isPalindrome(strInput):
    strInput = strInput.lower()

    i = 0
    while (i < len(strInput)):
        if (strInput[i].isalpha()):
            i += 1
        else:
            strInput = strInput.replace(strInput[i], '')

    return strInput == strInput[::-1]

string = input()
print(isPalindrome(string))


# Provided Solution - made note for future reference

# import re

# def is_palindrome(phrase):
#     forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
#     backwards = forwards[::-1]
#     return forwards == backwards
