# 51. N-Queens

# Hard

# Companies:
# Samsung
# Google
# Flipkart
# Amazon
# Microsoft
# Netflix
# Tekion-corp
# Bloomberg
# Oracle
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]
 

# Constraints:

# 1 <= n <= 9

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def valid(x,y,arr,n):
            # top-left-diagonal
            row=x
            col=y
            while row>=0 and col>=0:
                if arr[row][col]=="Q":
                    return False
                row-=1
                col-=1
                
            # bottom-left-diagonal
            row=x
            col=y
            while row<n and col>=0:
                if arr[row][col]=="Q":
                    return False
                row+=1
                col-=1
                
            # left-row
            row=x
            col=y
            while col>=0:
                if arr[row][col]=="Q":
                    return False
                col-=1
            return True
                
        def solve(col,arr=[["." for _ in range(n)] for _ in range(n)],res=[]):
            if col==n:
                res.append(["".join(arr[j]) for j in range(n)])
                return 
                
            
            for row in range(n):
                if valid(row,col,arr,n):
                    arr[row][col]="Q"
                    solve(col+1,arr,res)
                    arr[row][col]="."
            return res
        return solve(0)
    
    # time complexity: O(n!)
    # space complexity: O(n^2)