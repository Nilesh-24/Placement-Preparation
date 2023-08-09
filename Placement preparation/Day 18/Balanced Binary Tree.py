# 110. Balanced Binary Tree
# Easy

# Given a binary tree, determine if it is 
# height-balanced 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root)!=-1
    
    def height(self,root):
        if root is None:
            return 0
        hl=self.height(root.left)
        if hl==-1:
            return -1
        hr=self.height(root.right)
        if hr==-1:
            return -1
        if abs(hl-hr)>1:
            return -1
        return 1+max(hl,hr)
    
    # time complexity o(n)
    # space complexity o(n)