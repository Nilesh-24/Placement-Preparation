# 230. Kth Smallest Element in a BST

# Medium

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        a=deque([root])
        result=[]
        while a:
            node=a.popleft()
            result.append(node.val)
            if node.left:
                a.append(node.left)
            if node.right:
                a.append(node.right)
        result.sort()
        return result[-1+k]
    
# time complexity o(nlogn)
# space complexity o(n)