# Challenge: Write a Python function to count the number of unique words and how often each occurs.
# Input: path to a text file
# Output: print message with: - total number of words
#                             - top 20 most frequent words
#                             - number of occurrences for top 20
# Ignore case ("The" == "the"), words contain: letters, numbers, apostrophes, and hyphens

from re import findall
from collections import Counter

def countWords(path):
    data = open(path)
    allWords = findall(r"[a-zA-Z0-9'-]+", data.read())

    # Make all words lowercase to ignore case
    allWords = [word.lower() for word in allWords]

    countWords = Counter()
    for word in allWords:
        countWords[word] += 1


    # Output:

    print("Total Words:", len(allWords))

    print("\nTop 20 Words")
    for word in countWords.most_common(20):
        print("{}: {} time(s)".format(word[0], word[1]))

    data.close()

countWords("10 data.txt")
