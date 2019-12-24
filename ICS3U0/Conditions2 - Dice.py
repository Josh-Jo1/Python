#conditions2 - Dice

import random

print("Would you like to roll the dice?")

roll = input("\n'Yes' or 'No': ")

while roll == "Yes" or roll == "yes":

    dice = str(random.randint(1,6))
    print("\n" + dice)

    print("\nWould you like to roll the dice again?")

    roll = input("\n'Yes' or 'No': ")
