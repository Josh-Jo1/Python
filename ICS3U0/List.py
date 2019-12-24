#list
#Joshua Johnson
#March 5, 2018

import time

print("Opening markbook...")
time.sleep(2)

counter = 0

students = int(input("\nHow many students do you have? "))

allstudents = []
names = []

while students > counter:
    name = input("What is the student's name? ")
    mark = int(input("What is the student's mark? "))
            
    student = [name, mark]

    allstudents.append(student)
    counter += 1
        
print(allstudents)

time.sleep(2)

print("\nWould you like to modify this list?")
modify = input("'Yes' or 'No': ").lower()

while modify == "yes":

    print('''
    Here are the possible modifications:
    1. Sort the list by name.
    2. Add an item to the list.
    3. Delete an item from the list.
    4. Find an item in the list.
    5. Create a new list of only names.''')

    option = int(input("\nNumerical option: "))

    if option == 1:
        print("\nSorting...")
        time.sleep(2)
        allstudents.sort()
        print(allstudents)
        time.sleep(1)
        print("\nWould you like to modify the list again?")
        modify = input("'Yes' or 'No': ").lower()

    elif option == 2:
        addname = input("Student Name: ")
        addmark = int(input("Student Mark: "))
        addstudent = [addname, addmark]
        allstudents.append(addstudent)
        print("\nAdding...")
        time.sleep(2)
        print(allstudents)
        time.sleep(1)
        print("\nWould you like to modify the list again?")
        modify = input("'Yes' or 'No': ").lower()

    elif option == 3:
        delname = input("Student Name: ")
        for x in allstudents:
            for y in x:
                if delname == y:
                    allstudents.remove(x)
                    print("\nDeleting...")
                    time.sleep(2)
                    print(allstudents)
        time.sleep(1)
        print("\nWould you like to modify the list again?")
        modify = input("'Yes' or 'No': ").lower()

    elif option == 4:
        findname = input("Student Name: ")
        for x in allstudents:
            for y in x:
                if y == findname:
                    print("\nFinding...")
                    time.sleep(2)
                    print(x)
        time.sleep(1)
        print("\nWould you like to modify the list again?")
        modify = input("'Yes' or 'No': ").lower()

    elif option == 5:
        names.clear()
        for x in allstudents:
            for y in x:
                y = str(y)
                if y.isalpha():
                    names.append(y)
        print("\nCreating...")
        time.sleep(2)
        print(names)
        time.sleep(1)
        print("\nWould you like to modify the list again?")
        modify = input("'Yes' or 'No': ").lower()



