# 200. Number of Islands

# Medium

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        res=0
        def dfs(i,j):
            if grid[i][j]=="1":
                grid[i][j]="x"
                if j<n-1:
                    dfs(i,j+1)
                if j>0:
                    dfs(i,j-1)
                if i>0:
                    dfs(i-1,j)
                if i<m-1:
                    dfs(i+1,j)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    res+=1
                    dfs(i,j)

        return res

# time complexity: O(m*n)
# space complexity: O(m*n)