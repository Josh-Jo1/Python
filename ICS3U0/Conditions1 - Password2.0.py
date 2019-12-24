#conditions1 - Password2.0

import time

password = input("Create a password: ")
password2 = input("Confirm your password: ")

while password == password2:

    time.sleep(2)
    print("\nTwo days later...")
    time.sleep(2)

    x = 0
    
    while x < 3:
    
        attempt = input("\nEnter your password: ")

        if attempt != password:
            print("\nIncorrect password.")
            x = x + 1
            
        else:
            print("\nYou have successfully logged in!")
            break
            
    else:
        print("\nYou have been denied access!")
        break
    break
else:
    print("\nYou failed to confirm your password.")
    print("You are doomed to forget it!")
