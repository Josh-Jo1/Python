#practicalTest
#Joshua Johnson
#March 8, 2018

print("Enter a word to see what it looks like in the Canadian English!")
print('To quit, type in "quit!" when prompted to enter a word.')

def word(string):
    while len(string)>=4 and len(string)<=64:
        if string == "quit!" or string == "quit":
            print("Thank you for using this translator. Hope it helped!")
            quit()
        else:
            if string[-2:] == "or":
                newstring = string.replace("or", "our")
                print(newstring)
                word(input("\nEnter a word: "))
            else:
                print(string)
                word(input("\nEnter a word: "))
    else:
        print(string)
        word(input("\nEnter a word: "))
        
word(input("\nEnter a word: "))
