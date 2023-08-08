# 31. Next Permutation

# Medium

# Companies:
# Adobe
# Oracle
# Microsoft
# Netflix
# Google
# Samsung
# Walmart
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        # [1,2,3,4] -> [1,2,4,3]
        #[4, 3, 6, 7, 2] -> [4,3,7,2,6]
            
        if len(nums) == 1:
            return 
        
        if len(nums) == 2:
            nums.reverse()
            return
        
        i = len(nums)-1
        found = False
        
        #find first decreasing element from end
        while i >= 1:
            if nums[i] > nums[i-1]:
                found = True
                break
            i-=1
        if not found:
            nums.reverse()
            return
        j = i  #element just above first decreasing
        i-=1 #decrement to get decreasing element
        
        
        min_greater_than_i = float('inf')
        min_index = -1 
        while j <= len(nums)-1:
            if nums[j] > nums[i]:
                if nums[j] <= min_greater_than_i: #= check in case of duplicates: swap with last largest increasing value so that when reversed, in ascending order
                    min_greater_than_i = nums[j]
                    min_index = j
            j+=1
                

        nums[i], nums[min_index] = nums[min_index], nums[i]
        nums[i+1:] = reversed(nums[i+1:]) #nums[i+1:].reverse() doesn't work as splicing creates deep copy

#time complexity: O(n)
#space complexity: O(1)