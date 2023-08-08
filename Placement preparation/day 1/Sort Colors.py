# 75. Sort Colors

# Medium

# Companies

# Google
# Amazon
# Microsoft
# Netflix
# Tekion-corp
# Flipkart
# Bloomberg
# Samsung
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM
# Byju's

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Two pointer approach
        # Keep track of the position of 0s and 2s and swap the rest of the elements to their correct positions
        left = 0
        right = len(nums) - 1
        current = 0
        
        while current <= right:
            if nums[current] == 0:
                nums[current], nums[left] = nums[left], nums[current]
                left += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                current += 1

# Time Complexity: O(n)
# Space Complexity: O(1)