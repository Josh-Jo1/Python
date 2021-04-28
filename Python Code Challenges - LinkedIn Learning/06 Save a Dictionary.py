# Save Function
# Challenge: Write a Python function to save a dictionary to file.
# Input: dictionary to save, output file path

# Load Function
# Challenge: Write a Python function to load the saved dictionary back into Python.
# Input: file path to saved dictionary;   Output: retrieved dictionary object

def SaveFunction(dictInput, path):
    file = open(path, 'w')
    file.write(str(dictInput))
    file.close()

def LoadFunction(path):
    file = open(path, 'r')
    content = eval(file.read())
    file.close()
    return content, type(content)           # type function only included to show output is dict

dictionary = eval(input())
filePath = input()
# dictionary = {1: 'a', 2: 'b', 3: 'c'}
# filePath = "C:\\Python\\Saved Dictionary.txt"

SaveFunction(dictionary, filePath)
print(LoadFunction(filePath))
