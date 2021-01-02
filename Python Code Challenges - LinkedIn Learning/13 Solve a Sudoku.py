# Challenge: Write a Python function to solve a sudoku puzzle. Note that a well-designed puzzle will have 1 unique solution.
# Input: 2D list of lists (9 sublists with 9 elements each to represent puzzle), where 0 indicates an empty space
# Output: Solved sudoku puzzle

# Thought-process for solution:
# At any given moment, an unsolved, well-designed puzzle will have at least 1 square with only 1 valid number possible.
# After setting this square to its valid number, repeat the process to find at least 1 other square until puzzle is solved.


# For easier understanding, I created a separate function that determines the valid number of a given square
def validNumber(puzzle, row, col):
    num = 0
    
    for x in range(1,10):
        valid = True

        # Check row and column
        for y in range(0,9):
            if puzzle[row][y] == x or puzzle[y][col] == x:
                valid = False
                break

        # Check 3x3 box
        for m in range(0,3):
            for n in range(0,3):
                if puzzle[row//3*3 + m][col//3*3 + n] == x:
                    valid = False
                    break
        
        if valid:
            if num == 0: num = x
            else: return 0              # if multiple values possible in same square, return 0 and check again next loop

    return num      # this will be reached when only 1 value can be placed in a sqaure


def solveSudoku(puzzle):
    incomplete = True

    while incomplete:
        incomplete = False

        for r in range(0,9):
            for c in range(0,9):
                if puzzle[r][c] == 0:
                    incomplete = True

                    puzzle[r][c] = validNumber(puzzle, r, c)

    print(puzzle)


puzzle = [  [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]

solveSudoku(puzzle)

# This solution works for easy puzzles, like the test puzzle provided in the course.
# Once I complete the course, I will work on an improved solution to solve a Sudoku more efficiently.
