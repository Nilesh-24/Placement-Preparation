# 128. Longest Consecutive Sequence

# Medium

# Companies:
# Walmart
# Amazon
# Samsung
# Tekion-corp
# Flipkart
# Bloomberg
# Microsoft
# Adobe
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM
# Byju's

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        longest_sequence = 0
        for num in nums:
            if num - 1 in num_set:
                continue
            current_length = 1
            while num + 1 in num_set:
                num += 1
                current_length += 1
            longest_sequence = max(longest_sequence, current_length)
        return longest_sequence
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)