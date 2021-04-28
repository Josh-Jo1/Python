#stringManipulation

import time

print("This is a program to change, check, count, and search things in a word.")
time.sleep(3)
print("\nDo you wish to proceed?")
retry = input("'Yes' or 'No': ")

while retry == "Yes" or retry == "yes":
    
    word = input("\nEnter a word: ")
    print('''
Here are your options:
    1. Change to either uppercase or lowercase
    2. Check to see if string has any numbers
    3. Count number of characters
    4. Search for a letter and return the position
''')
    option = input("\nWhich option number would you like to execute? ")

    if option == "1":
        change = input("\n'Uppercase' or 'Lowercase': ")

        if change == "Uppercase" or change == "uppercase":
            print("\nChanging...")
            time.sleep(2)
            print("\nYour word is now...")
            print(word.upper())
            print("\nDo you want to try again?")
            retry = input("'Yes' or 'No': ")

        elif change == "Lowercase" or change == "lowercase":
            print("\nChanging...")
            time.sleep(2)
            print("\nYour word is now...")
            print(word.lower())
            print("\nDo you want to try again?")
            retry = input("'Yes' or 'No': ")

        else:
            print("\nYour input was invalid.")
            print("\nDo you want to try again?")
            retry = input("'Yes' or 'No': ")

    elif option == "2":
        check = word.isalpha()
        
        if check == True:
            print("\nChecking...")
            time.sleep(2)
            print("\nYour word does not have any numbers.")
            print("\nDo you want to try again?")
            retry = input("'Yes' or 'No': ")
            
        else:
            print("\nChecking...")
            time.sleep(2)
            print("\nYour word does have numbers.")
            print("\nDo you want to try again?")
            retry = input("'Yes' or 'No': ")

    elif option == "3":
        print("\nCounting...")
        time.sleep(2)
        count = len(word)
        print("\nYour word is", count, "characters long.")
        print("\nDo you want to try again?")
        retry = input("'Yes' or 'No': ")

    elif option == "4":
        search = input("\nEnter the character you wish to find: ")
        position = int(word.find(search))
        print("\nSearching...")
        time.sleep(2)
        
        if position >= 0:
            print("\nThe first position of character '" + search + "' is", position + 1)
            print("In code, this is actually position", position)
            print("\nDo you want to try again?")
            retry = input("'Yes' or 'No': ")

        else:
            print("\nThis character cannot be found in your code.")
            print("\nDo you want to try again?")
            retry = input("'Yes' or 'No': ")

    else:
        print("Your input was invalid.")
        print("\nDo you want to try again?")
        retry = input("'Yes' or 'No': ")    




