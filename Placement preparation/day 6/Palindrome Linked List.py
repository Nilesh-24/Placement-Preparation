# 234. Palindrome Linked List

# Easy

# Companies:
# Netflix
# Bloomberg
# Walmart
# Samsung
# Amazon
# Adobe
# Oracle
# Microsoft
# Tekion-corp
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM
# Byju's

# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def check(head):
            if (head == None):
                return True
            res = check(head.next) and (self.temp.val == head.val)
            self.temp = self.temp.next
            return res
        
        self.temp = head
        return check(head)
    
# time complexity: O(n)
# space complexity: O(n)