# Challenge specified in LinkedinIn video. Refer to README file for more information.

from random import randint
from time import time

def WaitingGame():
    target = randint(2,4)
    print("Your target time is {} seconds.".format(target))
    
    input(" ---Press Enter to Begin--- ")
    start = time()

    input("\n...Press Enter again after {} seconds...".format(target))

    elapsedTime = round(time() - start, 3)
    targetMiss = round(elapsedTime - target, 3)
    targetMissMessage = ""

    if (target == elapsedTime):
        targetMissMessage = "(Right on time)"
    elif (targetMiss > 0):
        targetMissMessage = "({} seconds too slow)".format(targetMiss)
    else:
        targetMissMessage = "({} seconds too fast)".format(-targetMiss)

    print("\nElapsed time: {} seconds {}".format(elapsedTime, targetMissMessage))

WaitingGame()
