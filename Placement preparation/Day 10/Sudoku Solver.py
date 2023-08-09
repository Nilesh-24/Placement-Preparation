# 37. Sudoku Solver

# Hard

# Companies:
# Amazon
# Walmart
# Tekion-corp
# Oracle
# Adobe
# Google
# Facebook
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

 

# Example 1:


# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:


 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def isValid(board:List[List[str]], row:int, col:int, val:str) -> bool:
            
            for i in range(0, 9):
                if board[i][col]==val: return False
                if board[row][i]==val: return False
            
            for limit in range(3, 10, 3):
                if row < limit: 
                    rowLimit = limit
                    break
            for limit in range(3, 10, 3):
                if col < limit:
                    colLimit = limit
                    break
            for i in range(rowLimit-3, rowLimit):
                for j in range(colLimit-3, colLimit):
                    if board[i][j]==val: return False
            
            return True

        def sudoku(board:List[List[str]]):
            for i in range(0, 9):
                for j in range(0, 9):
                    
                    if board[i][j] == ".":
                        for val in range(1, 10):
                            if isValid(board, i, j, str(val)):
                                board[i][j] = str(val)
                                if sudoku(board) == True:
                                    return True
                                board[i][j] = "."
                        return False
            return True
        sudoku(board)
        return board
    
    # time complexity: O(9^(n*n))
    # space complexity: O(n*n)