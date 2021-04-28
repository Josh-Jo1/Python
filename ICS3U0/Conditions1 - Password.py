#conditions1 - Password

import time

password = input("Create a password: ")
password2 = input("Confirm your password: ")

while password == password2:

    time.sleep(3)
    print("\nTwo days later...")
    attempt1 = input("\nEnter your password: ")

    if attempt1 == password:
        print("\nYou have successfully logged in!")
    else:
        print("\nIncorrect password. Please try again.")
        attempt2 = input("\nEnter your password: ")
        break

        if attempt2 == password:
            print("\nYou have successfully logged in!")
        else:
            print("\nIncorrect password. Please try again.")
            attempt3 = input("\nEnter your password: ")
            break

            if attempt3 == password:
                print("\nYou have successfully logged in!")
            else:
                print("\nIncorrect password. You have been denied access!")
                break

else:
    print("You failed to confirm your password.")
    print("You are doomed to forget it!")
