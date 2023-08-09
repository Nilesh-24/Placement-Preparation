# Kth largest element in BST

# Easy

# Given a Binary search tree. Your task is to complete the function which will return the Kth largest element without doing any modification in Binary Search Tree.


# Example 1:

# Input:
#       4
#     /   \
#    2     9
# k = 2 
# Output: 4

# Example 2:

# Input:
#        9
#         \ 
#           10
# K = 1
# Output: 10

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function kthLargest() which takes the root of the BST and an integer K as inputs and returns the Kth largest element in the given BST.


# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(H) where H is max recursion stack of height h at a given time.


# Constraints:
# 1 <= N <= 1000
# 1 <= K <= N

#User function Template for python3

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root, k):
        def reverse_inorder(node):
            nonlocal k
            if node is None or k <= 0:
                return None

            result = reverse_inorder(node.right)

            if k == 0:
                return result

            k -= 1

            if k == 0:
                return node.data  
            return reverse_inorder(node.left)

        return reverse_inorder(root)
    
    # time complexity: O(h+k)
    # space complexity: O(h)