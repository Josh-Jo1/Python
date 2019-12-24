#introToFunctions

def x(string):

    upperCase = 0
    lowerCase = 0
    numbers = 0
    spaces = 0
    for i in string:
        if i.isupper():
            upperCase += 1
        if i. islower():
            lowerCase += 1
        if i. isnumeric():
            numbers += 1     
        if i. isspace():
            spaces += 1

    print("\nThere are", upperCase, "uppercase character(s).")
    print("There are", lowerCase, "lowercase character(s).")
    print("There are", numbers, "numerical character(s).")
    print("There are", spaces, "space(s).")

string = input("Enter a string: ")

x(string)
