# 152. Maximum Product Subarray
# Medium

# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums):
        cuml_max = cuml_min= max_sofar = nums[0]
        for i, num in enumerate(nums[1:], start=1):
            prv_cuml_min = cuml_min  
            cuml_min = min(cuml_min*num, cuml_max*num, num)
            cuml_max = max(prv_cuml_min*num, cuml_max*num, num) 
            max_sofar = max(cuml_max, max_sofar)
        return max_sofar
    
# Time Complexity: O(n)
# Space Complexity: O(1)