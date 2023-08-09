# 686. Repeated String Match
# Medium

# Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

# Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

 

# Example 1:

# Input: a = "abcd", b = "cdabcdab"
# Output: 3
# Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
# Example 2:

# Input: a = "a", b = "aa"
# Output: 2
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist of lowercase English letters.

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        for i in range(len(b) // len(a) + 3):
            if b in a*i: return i
        return -1
    
    # time complexity O(n)
    # space complexity O(n)