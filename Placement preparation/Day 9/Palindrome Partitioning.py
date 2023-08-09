# 131. Palindrome Partitioning

# Medium

# Companies:
# Oracle
# Facebook
# Tekion-corp
# Adobe
# Flipkart
# Bloomberg
# Netflix
# Amazon
# Walmart
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo

# Given a string s, partition s such that every 
# substring
#  of the partition is a 
# palindrome
# . Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def extend(i, cur):
            if i >= len(s):
                res.append(cur[::])
            p = ''
            for j in range(i, len(s)):
                p += s[j]
                if p == p[::-1]:
                    extend(j + 1, cur + [p])
        
        extend(0, [])
        return res
    
    # time complexity: O(n*2^n)
    # space complexity: O(n)