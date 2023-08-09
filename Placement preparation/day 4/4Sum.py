# 18. 4Sum

# Medium

# Companies:
# Microsoft
# Samsung
# Walmart
# Flipkart
# Oracle
# Google
# Netflix
# Adobe
# Amazon
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        new_s = []
        for i in range(len(nums)-3):
            for k in range(len(nums)-1,i,-1):
                left = i + 1
                right = k - 1
                while left<right:
                    if nums[right]+nums[k]+nums[i]+nums[left] == target and [nums[i],nums[left],nums[right],nums[k]] not in new_s:
                        new_s.append([nums[i],nums[left],nums[right],nums[k]])
                    if nums[right]+nums[k]+nums[i]+nums[left]<=target:
                        left += 1
                    else:
                        right -= 1
        return new_s
    

    #time complexity: O(n^3)
    #space complexity: O(n)