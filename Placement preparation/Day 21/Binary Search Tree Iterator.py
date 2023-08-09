# 173. Binary Search Tree Iterator

# Medium

# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

# Example 1:

# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]

# Explanation
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False
 
# Constraints:

# The number of nodes in the tree is in the range [1, 105].
# 0 <= Node.val <= 106
# At most 105 calls will be made to hasNext, and next.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.iter = iter(self.iterativeInorder())
        self.nextValue = -1

    def iterativeInorder(self) :
        stack = []
        curr = self.root
        while True :
            if curr is not None :
                stack.append(curr)
                curr = curr.left

            elif stack :
                curr = stack.pop()
                yield curr.val
                curr = curr.right

            else :
                break

        return -1

    def next(self) -> int:
        if self.nextValue >= 0 :
            res = self.nextValue
            self.nextValue = -1
            return res 

        else :
            return next(self.iter)

    def hasNext(self) -> bool:
        if self.nextValue >= 0 : return True
        try :
            self.nextValue = next(self.iter)
            return True
        except StopIteration :
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# time complexity o(n)
# space complexity o(n)