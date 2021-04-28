# Input: 2D array (each array has 9 elements) to represent unsolved Sudoku puzzle.
# A well-designed puzzle will have 1 unique solution.
# Let 0 indicate an empty square.


# Test cases:

easyPuzzle = [  [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# Solution:     [5, 3, 4, 6, 7, 8, 9, 1, 2]
#               [6, 7, 2, 1, 9, 5, 3, 4, 8]
#               [1, 9, 8, 3, 4, 2, 5, 6, 7]
#               [8, 5, 9, 7, 6, 1, 4, 2, 3]
#               [4, 2, 6, 8, 5, 3, 7, 9, 1]
#               [7, 1, 3, 9, 2, 4, 8, 5, 6]
#               [9, 6, 1, 5, 3, 7, 2, 8, 4]
#               [2, 8, 7, 4, 1, 9, 6, 3, 5]
#               [3, 4, 5, 2, 8, 6, 1, 7, 9]


mediumPuzzle = [[9, 0, 0, 0, 3, 4, 0, 0, 0],
                [2, 3, 0, 0, 9, 0, 0, 1, 0],
                [0, 0, 0, 2, 0, 0, 7, 0, 0],
                [6, 1, 0, 5, 0, 2, 0, 3, 7],
                [0, 0, 0, 0, 8, 0, 0, 0, 0],
                [4, 9, 0, 3, 0, 7, 0, 2, 1],
                [0, 0, 3, 0, 0, 8, 0, 0, 0],
                [0, 2, 0, 0, 5, 0, 0, 7, 4],
                [0, 0, 0, 4, 7, 0, 0, 0, 2]]

# Solution:     [9, 6, 1, 7, 3, 4, 2, 5, 8]
#               [2, 3, 7, 8, 9, 5, 4, 1, 6]
#               [5, 8, 4, 2, 1, 6, 7, 9, 3]
#               [6, 1, 8, 5, 4, 2, 9, 3, 7]
#               [3, 7, 2, 9, 8, 1, 6, 4, 5]
#               [4, 9, 5, 3, 6, 7, 8, 2, 1]
#               [7, 4, 3, 1, 2, 8, 5, 6, 9]
#               [8, 2, 9, 6, 5, 3, 1, 7, 4]
#               [1, 5, 6, 4, 7, 9, 3, 8, 2]


hardPuzzle = [  [8, 2, 0, 0, 0, 9, 0, 0, 0],
                [0, 6, 0, 4, 0, 0, 3, 0, 0],
                [0, 0, 9, 0, 8, 0, 1, 0, 0],
                [0, 0, 0, 5, 0, 0, 0, 0, 3],
                [5, 0, 2, 0, 0, 0, 7, 0, 1],
                [4, 0, 0, 0, 0, 6, 0, 0, 0],
                [0, 0, 3, 0, 6, 0, 8, 0, 0],
                [0, 0, 1, 0, 0, 3, 0, 5, 0],
                [0, 0, 0, 9, 0, 0, 0, 3, 2]]

# Solution:     [8, 2, 4, 1, 3, 9, 5, 7, 6]
#               [1, 6, 5, 4, 7, 2, 3, 9, 8]
#               [3, 7, 9, 6, 8, 5, 1, 2, 4]
#               [6, 1, 8, 5, 9, 7, 2, 4, 3]
#               [5, 9, 2, 3, 4, 8, 7, 6, 1]
#               [4, 3, 7, 2, 1, 6, 9, 8, 5] 
#               [2, 5, 3, 7, 6, 4, 8, 1, 9]
#               [9, 4, 1, 8, 2, 3, 6, 5, 7]
#               [7, 8, 6, 9, 5, 1, 4, 3, 2]

##################################################################################################################################

# Method 1
# From Python Code Challenges - LinkedIn Learning (Challenge 13)

# Assuming there is at least 1 box at any given moment that could be filled with a number, I came up with the following solution:


# def validNumber(puzzle, row, col):
#     num = 0
    
#     for x in range(1,10):
#         valid = True

#         # Check row and column
#         for y in range(0,9):
#             if puzzle[row][y] == x or puzzle[y][col] == x:
#                 valid = False
#                 break

#         # Check 3x3 box
#         for m in range(0,3):
#             for n in range(0,3):
#                 if puzzle[row//3*3 + m][col//3*3 + n] == x:
#                     valid = False
#                     break
        
#         if valid:
#             if num == 0: num = x
#             else: return 0              # if multiple values possible in same square, return 0 and check again next loop

#     return num      # this will be reached when only 1 value can be placed in a sqaure


# def solveSudoku(puzzle):
#     incomplete = True

#     while incomplete:
#         incomplete = False

#         for r in range(0,9):
#             for c in range(0,9):
#                 if puzzle[r][c] == 0:
#                     incomplete = True

#                     puzzle[r][c] = validNumber(puzzle, r, c)

#     print(puzzle)


# solveSudoku(easyPuzzle)


# While this solution will work for some (easy) Sudoku puzzles, it will not work for most (difficult) ones.
# For this reason, I wanted to write a more thorough and complete solution.

##################################################################################################################################

# Method 2 - Backtracking

from itertools import product

def solveSudoku(puzzle):
    for (row, col) in product(range(0,9), repeat=2):        # this is equivalent to nested for loops to search rows and columns
        if puzzle[row][col] == 0:
            
            # Find valid number for that square
            for x in range(1,10):
                valid = True

                # Check row and column
                for i in range(0,9):
                    if puzzle[row][i] == x or puzzle[i][col] == x:
                        valid = False
                        break

                if valid:                   # if valid is false, there is no need to check box anymore
                    # Check 3x3 box
                    for (m,n) in product(range(0,3), repeat=2):
                        if puzzle[row//3*3 + m][col//3*3 + n] == x:
                            valid = False
                            break

                if valid:
                    puzzle[row][col] = x            # set current cell to valid number (x)
                    trial = solveSudoku(puzzle)     # use that number to continue finding solution
                    
                    if trial: return trial          # if trial passes, return it
                    else: puzzle[row][col] = 0      # if trial fails, set cell back to 0

            return False    # if no valid number goes in cell, need to backtrack
    
    return puzzle   # when solution is found, there will be no zeros in puzzle, so return completed puzzle


def printSolution(solution):
    for row in solution:
        print(row)
    print("")


print("Easy Puzzle Solution:")
printSolution(solveSudoku(easyPuzzle))
print("Medium Puzzle Solution:")
printSolution(solveSudoku(mediumPuzzle))
print("Hard Puzzle Solution:")
printSolution(solveSudoku(hardPuzzle))


# Method 2 is a significantly improved solution and will cover MOST well-designed Sudoku puzzles.
# Due to the process of attempting every possible number for each empty square (from top to bottom),
# puzzles can be created to work against the Backtracking method and require lots of time to run,
# such as the following puzzle:
#             [0, 0, 0, 0, 0, 0, 0, 0, 0]
#             [0, 0, 0, 0, 0, 3, 0, 8, 5]
#             [0, 0, 1, 0, 2, 0, 0, 0, 0]
#             [0, 0, 0, 5, 0, 7, 0, 0, 0]
#             [0, 0, 4, 0, 0, 0, 1, 0, 0]
#             [0, 9, 0, 0, 0, 0, 0, 0, 0]
#             [5, 0, 0, 0, 0, 0, 0, 7, 3]
#             [0, 0, 2, 0, 1, 0, 0, 0, 0]
#             [0, 0, 0, 0, 4, 0, 0, 0, 9]

# However, the Backtracking method remains to be an efficient way to complete a general Sudoku puzzle.
