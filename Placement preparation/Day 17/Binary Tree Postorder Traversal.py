# 145. Binary Tree Postorder Traversal

# Easy

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

class Solution(object):
    def postorderTraversal(self, root):
        if root is None:
            return []
        traveral = []
        stack = [root]
        while(len(stack) > 0):
            if stack[-1].left is not None:
                stack.append(stack[-1].left)
                stack[-2].left = None
            elif stack[-1].right is not None:
                stack.append(stack[-1].right)
                stack[-2].right = None
            else:
                traveral.append(stack.pop().val)
            
        return traveral
    
    # time complexity O(n)
    # space complexity O(n)