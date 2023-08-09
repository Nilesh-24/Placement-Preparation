# 102. Binary Tree Level Order Traversal
# Medium

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def solve(k):
            if len(k)==0:
                return
            
            ans , newk= [], []
            for node in k:
                ans.append( node.val )
                
                if node.left:
                    newk.append(node.left)
                if node.right:
                    newk.append(node.right)
            
            res.append(ans)
            solve( newk )
            return
        
        res = []
        if root:
            solve( [root] )
        return res
    
    # time complexity o(n)
    # space complexity o(n)