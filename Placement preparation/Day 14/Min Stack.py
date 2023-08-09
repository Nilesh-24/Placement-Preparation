# 155. Min Stack

# Medium

# Companies:
# Tekion-corp
# Adobe
# Netflix
# Bloomberg
# Facebook
# Oracle
# Google
# Microsoft
# Flipkart
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM
# Byju's`

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

class Node:
    def __init__(self, val=None, mini=None, next=None):
        self.val = val
        self.minimum = mini
        self.next = next

class MinStack:

    def __init__(self):
        self.head = None
        

    def push(self, x: int) -> None:
        if self.head is None:
            node = Node(x, x)
            self.head = node
        else:
            node = Node(x, min(x, self.head.minimum), self.head)
            self.head = node
        

    def pop(self) -> None:
        self.head = self.head.next
        

    def top(self) -> int:
        return self.head.val
        

    def getMin(self) -> int:
        return self.head.minimum
    
    # time complexity: O(1)
    # space complexity: O(n)