#chooseYourOwnAdventure

import time

print("Thus begins the game that will decide your fate,")
print("Choose wisely, my friend, and do not be quick to hate.")
print("Trust yourself and beware my bait,")
print("Best of all, this will be great!")

time.sleep(8)

print("\nDo you want to play?")
x = input("'Yes' or 'No'? ")

while x == "Yes" or x == "yes":

    Name = input("\nPick a name: ")
    Place = input("Pick a city: ")

    time.sleep(3)

    print("\nIt was a morning like no other for", Name, "of", Place, "as they walked out of their house.")
    print("'Good morning neighbor. How was your weekend?'")
    print("'It was great. I held a party, but unfortunately someone broke my couch. Can you help me fix it?' said the neighbor.")

    time.sleep(10)

    Fix = input("\n'Yes' or 'No': ")

    if Fix == "Yes" or Fix == "yes":
        print("\n'Sure thing.'")
        print("You proceed towards the house. You see a car go by at full speed and hope no one gets hurt.")
        print("Once inside the house, you find the broken couch with a screwdriver to the left and a box labelled tools further off to the right.")
        time.sleep(10)

        print("\n'The damn recliner won't go back down. You can use any tools that you may need. Thank you.'")
        print("\nWhat do you take?")

        Tool = input("\n'Screwdriver' or 'Box labelled tools': ")

        if Tool == "Screwdriver" or Tool == "screwdriver":
            print("\nWise choice! you unscrew a broken bolt and replace it with a new one.")
            print("'Thank you so much", Name, "for your help. I couldn't even see the bolt there. Have a great day!'")
            print("You leave the house with a smile on your face and continue your day.")
            time.sleep(10)

            print("\nAfter a long day of work, you return home with sleep on your mind. At your doorstep, you find a present.")
            print("It has the words 'Thanks again' written on it followed by 'open this before 9pm.'")
            print("\nDo you open it now or go to sleep?")

            Present = input("\n'Open now' or 'Sleep': ")

            if Present == "Open now" or Present == "open now":
                print("\nYou find the replaced bolt with a bow tied around it. Also inside the box is a note.")
                print("It says your neighbor is having a party tonight and you are invited. You decide to treat yourself and go.")
                print("About half an hour after you reach, the police arrives and arrests everyone.")
                print("Turns out there were drugs in the house from the party the night before and someone had snitched.")
                time.sleep(20)

                print("\nYou may not have been killed that night, but the arrest goes on your record and you get fired from your job.")
                print("\nDo you want to play again?")
                x = input("'Yes' or 'No': ")

            else:
                print("\nYou have a quick dinner and get a good night's rest. In the morning, you open the present and find the replaced bolt with a bow tied around it.")
                print("Also inside the box is a note that says your neighbor had another party last night and you were invited. Too bad you couldn't go, but at least you slept well.")
                time.sleep(7)

                print("\nYou have survived many things! Well done!")
                print("\nDo you want to play again?")
                x = input("'Yes' or 'No': ")
        
        else:
            print("\nYou open the box to find packages of cocaine. Hoping the neighbor was not watching, you close the lid and return for the screwdriver.")
            print("That's when everything goes black and you are lost forever.")
            time.sleep(4)

            print("\nDo you want to play again?")
            x = input("'Yes' or 'No': ")
                
    else:
        print("\n'Sorry, I'm busy today. I have to go to a funeral.'")
        print("'I'm so sorry to hear. Who's funeral is it?'")
        time.sleep(5)

        print("\nAt that moment a car rushes across the street and slams you to the ground.")

        print("\nI suppose you will be going to your own funeral.")
        print("\nDo you want to play again?")
        x = input("'Yes' or 'No': ")
    
