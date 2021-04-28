# Problem E
# Given a positive integer N, place N queens on an N*N chessboard such that no two queens attack each other. Return all possible solutions.

# Input a positive integer to solve puzzle or anything else to end program
myInput = input()


from copy import deepcopy

QUEEN = 1
SPACE = 0

def solveQueens(n, board, count, solutions):
    # Create board
    if board == []:
        for r in range(n):
            row = []
            for c in range(n):
                row.append(SPACE)
            board.append(row)
    
    if count == n:
        solutions.append(deepcopy(board))
        return False        # will set last element back to SPACE to continue finding solutions

    # Solve
    for i in range(n):
        board[count][i] = QUEEN
        allowed = True

        # Check column
        row = 0
        while allowed and row < n:
            if row != count and board[row][i] == QUEEN:
                allowed = False
                board[count][i] = SPACE
            row += 1
        
        # Check diagonal
        row = count - 1
        l_diag = i - 1
        r_diag = i + 1
        while allowed and (l_diag > -1 or r_diag < n):
            if l_diag > -1 and board[row][l_diag] == QUEEN:
                allowed = False
                board[count][i] = SPACE
            elif r_diag < n and board[row][r_diag] == QUEEN:
                allowed = False
                board[count][i] = SPACE
            row -= 1
            l_diag -= 1
            r_diag += 1
        
        if allowed:
            retval = solveQueens(n, board, count + 1, solutions)
            if retval == False:
                board[count][i] = SPACE
            else:
                return retval
    
    return False


def printSolutions(rows, solutions):
    totalSolutions = len(solutions)     # variable for efficiency
    for i in range(totalSolutions):
        print(f"Solution {i + 1}:")
        for r in range(rows):
            print(solutions[i][r])


while (myInput.isnumeric()):
    N = int(myInput)
    if N < 1:
        print("This is not a positive integer")
    elif N == 1:
        print([1])
    elif N == 2 or N == 3:
        print("No solution")
    else:
        puzzleSolutions = []
        solveQueens(N, [], 0, puzzleSolutions)      # modifies puzzleSolutions
        printSolutions(N, puzzleSolutions)
    
    print("")               # print spacing between solutions
    myInput = input()
