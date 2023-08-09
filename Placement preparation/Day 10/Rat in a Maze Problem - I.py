# Rat in a Maze Problem - I

# Medium

# Companies:
# Walmart
# Samsung
# Netflix
# Facebook
# Tekion-corp
# Google
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi

# Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
# Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

# Example 1:

# Input:
# N = 4
# m[][] = {{1, 0, 0, 0},
#          {1, 1, 0, 1}, 
#          {1, 1, 0, 0},
#          {0, 1, 1, 1}}
# Output:
# DDRDRR DRDDRR
# Explanation:
# The rat can reach the destination at 
# (3, 3) from (0, 0) by two paths - DRDDRR 
# and DDRDRR, when printed in sorted order 
# we get DDRDRR DRDDRR.
# Example 2:
# Input:
# N = 2
# m[][] = {{1, 0},
#          {1, 0}}
# Output:
# -1
# Explanation:
# No path exists and destination cell is 
# blocked.
# Your Task:  
# You don't need to read input or print anything. Complete the function printPath() which takes N and 2D array m[ ][ ] as input parameters and returns the list of paths in lexicographically increasing order. 
# Note: In case of no path, return an empty list. The driver will output "-1" automatically.

# Expected Time Complexity: O((3N^2)).
# Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths.

# Constraints:
# 2 ≤ N ≤ 5
# 0 ≤ m[i][j] ≤ 1

class Solution:
    def isValidPath(self, m, n, ratX, ratY, visited):
        if (ratX >= 0 and ratX < n) and (ratY >= 0 and ratY < n) and visited[ratX][ratY] == 0 and m[ratX][ratY] == 1:
            return 1
        return 0
    
    def solveRat(self, m, n, visited, ratX, ratY, string, ans):
        # Base Condition.
        if ratX == n - 1 and ratY == n - 1:
            ans.append(string)
            return
        
        visited[ratX][ratY] = 1
        
        # Down
        if self.isValidPath(m, n, ratX + 1, ratY, visited):
            string += "D"
            self.solveRat(m, n, visited, ratX + 1, ratY, string, ans)
            string = string[:-1]
        
        # Left
        if self.isValidPath(m, n, ratX, ratY - 1, visited):
            string += "L"
            self.solveRat(m, n, visited, ratX, ratY - 1, string, ans)
            string = string[:-1]
        
        # Right
        if self.isValidPath(m, n, ratX, ratY + 1, visited):
            string += "R"
            self.solveRat(m, n, visited, ratX, ratY + 1, string, ans)
            string = string[:-1]
        
        # Up
        if self.isValidPath(m, n, ratX - 1, ratY, visited):
            string += "U"
            self.solveRat(m, n, visited, ratX - 1, ratY, string, ans)
            string = string[:-1]
        
        visited[ratX][ratY] = 0
    
    def findPath(self, m, n):
        if m[0][0] == 0:
            return ["-1"]
        
        visited = [[0 for _ in range(n)] for _ in range(n)]
        ans = []
        string = ""
        ratX, ratY = 0, 0
        
        self.solveRat(m, n, visited, ratX, ratY, string, ans)
        
        return ans

# time complexity: O((3N^2) * (L * X)), L = length of the path, X = number of paths.
# space complexity: O(N^2)