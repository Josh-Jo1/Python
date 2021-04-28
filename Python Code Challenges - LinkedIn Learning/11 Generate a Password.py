# Challenge: Write a Python function to generate passphrases.
# Must use Diceware Method (from https://theworld.com/~reinhold/diceware.html)
# Input: number of words in passphrase; Output: string of random words, separated by commas

from secrets import choice          # learned about this in documentation - same as random but increased security

def generatePassphrase(wordCount):
    with open("11 wordlist.asc") as wordsFile:
        fileLines = wordsFile.readlines()[2:7778]       # specific indexing based on worldlist file
        allWordsList = [line.split()[1] for line in fileLines]

    passphrase = [choice(allWordsList) for i in range(wordCount)]
    print(' '.join(passphrase))


generatePassphrase(int(input()))
# generatePassphrase(5)


# Provided solution is very similar to above
