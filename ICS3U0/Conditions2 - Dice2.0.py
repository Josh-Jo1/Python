#conditions2 - Dice2.0

import random
import time

print("Would you like to roll the dice?")

roll = input("\n'Yes' or 'No': ")

if roll == "Yes" or roll == "yes":

    print("\nTo stop, enter 'ctrl + c'.")

    try:
        while roll == "Yes" or roll == "yes":

            dice = str(random.randint(1,6))
            time.sleep(1)
            print("\nRolling...")
            time.sleep(1)
            print("\n" + dice)
            
    except KeyboardInterrupt:
        pass

