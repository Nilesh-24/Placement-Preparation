# 90. Subsets II
# Medium

# Companies:
# Netflix
# Adobe
# Samsung
# Bloomberg
# Google
# Walmart
# Flipkart
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi

# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        self.backtracking(res,0,[],nums)
        return res
    def backtracking(self,res,start,subset,nums):
        res.append(list(subset))
        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.backtracking(res,i+1,subset+[nums[i]],nums)

            # time complexity: O(2^n)
            # space complexity: O(n)