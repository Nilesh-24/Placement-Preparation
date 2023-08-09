# 61. Rotate List

# Medium

# Companies:
# Flipkart
# Amazon
# Walmart
# Google
# Oracle
# Netflix
# Samsung
# Bloomberg
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM
# Byju's

# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        start = ans =  head
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
            
        for i in range(k%len(lst)):
            p = lst.pop(-1)
            lst.insert(0 , p)
            
        while start:
            start.val = lst.pop(0)
            start = start.next
            
        return ans
    
# time complexity: O(n)
# space complexity: O(n)