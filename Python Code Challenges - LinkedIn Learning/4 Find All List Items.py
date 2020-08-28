# Challenge: Write a Python function to index all items in a list.
# Input: list to search, value to search for; Output: list of indices
# Keep in mind that lists can contain other lists

def findListItems(strList, indexList, index, item):
    for i in range(len(strList)):
        if isinstance(strList[i], list):
            findListItems(strList[i], indexList, index + [i], item)
        elif strList[i] == item:
            indexList.append(index + [i])

inputList = [[1, 2, 3, 4], 1, 2, 3, [4, 5, 2]]
searchItem = 2

# Also works for list of strings:
# inputList = [["hi", "hello"], "hola", ["bonjour", "salut"], "hello"]
# searchItem = "hello"

listOfIndices = []
findListItems(inputList, listOfIndices, [], searchItem)

print(listOfIndices)
