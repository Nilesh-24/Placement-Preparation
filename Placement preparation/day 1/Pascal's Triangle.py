# 118. Pascal's Triangle

# Easy

# Companies:

# Google
# Microsoft
# Tekion-corp
# Facebook
# Netflix
# Oracle
# Samsung
# Adobe
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM
# Byju's


# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:n

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30

class Solution:
  def generate(self, n: int) -> List[List[int]]:
    return list(accumulate([[1]]*n, lambda a,b: [x+y for x,y in zip(a+[0],[0]+a)]))
  
# accumulate function used to generate subsequent rows of Pascal's Triangle

#lambda function adds each pair of corresponding elements from the previous 
#     ->row (a) and its 
#      ->reverse (b), and generates a new row.


#time complexity: O(n^2)

#space complexity: O(n^2)