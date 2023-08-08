# 169. Majority Element

# Easy

# Companies:
# Flipkart
# Facebook
# Oracle
# Amazon
# Adobe
# Bloomberg
# Samsung
# Walmart
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM
# Byju's

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
    
    #Time Complexity: O(nlogn)
    #Space Complexity: O(1)