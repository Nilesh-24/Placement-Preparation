# Largest subarray with 0 sum
# Easy

# Companies:
# Adobe
# Walmart
# Netflix
# Samsung
# Microsoft
# Google
# Bloomberg
# Flipkart
# Amazon
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM
# Byju's

# Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

# Example 1:

# Input:
# N = 8
# A[] = {15,-2,2,-8,1,7,10,23}
# Output: 5
# Explanation: The largest subarray with
# sum 0 will be -2 2 -8 1 7.
# Your Task:
# You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).

# Constraints:
# 1 <= N <= 105
# -1000 <= A[i] <= 1000, for each valid i

class Solution:
    def maxLen(self, n, arr):
        #Code here
        max_length = 0
        sum = 0
        hashmap = {}
        for i in range(n):
            
            sum += arr[i]
            if sum == 0:
                max_length = i+1
                
            elif sum in hashmap:
                max_length = max(max_length,i-hashmap[sum])
            else:
                hashmap[sum] = i
        return max_length
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)