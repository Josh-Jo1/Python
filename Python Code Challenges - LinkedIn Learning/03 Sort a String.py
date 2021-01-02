# Challenge: Write a Python function to sort the words in a string.
# Input: string of words, separated by space;   Output: string of words, sorted alphabetically
# Ignore case when sorting, words in output string should have same case as input

def sortString(strInput):
    sortedString = strInput.split()
    sortedString.sort(key=lambda word: word.lower())
    return " ".join(sortedString)

string = input()
print(sortString(string))
