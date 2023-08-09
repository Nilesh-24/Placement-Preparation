# 101. Symmetric Tree
# Easy

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:

# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:

# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100

class Solution:
     def isSymmetric(self, root):
     
        if root == None:
            return True
        if root.right == None and root.left == None:
            return True
        if root.right == None or root.left == None:
            return False
        if root.right.val != root.left.val:
            return False
                            
        outer,inner=TreeNode(0),TreeNode(0)
        outer.right,outer.left=root.right.right,root.left.left
        inner.right,inner.left=root.right.left,root.left.right
        return self.isSymmetric(outer) and self.isSymmetric(inner)
     
        # time complexity o(n)
        # space complexity o(h)