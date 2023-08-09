# 297. Serialize and Deserialize Binary Tree

# Hard

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Example 1:

# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if root==None:
            return "x"
        return "["+str(root.val)+","+self.serialize(root.left)+","+self.serialize(root.right)+"]"
        
        

    def deserialize(self, data):
        if data=="x":
            return None
        else:
            #val
            val=int(data[1:data.find(",")])

            #left
            leftstart=data.index(',')+1
            if data[leftstart]=="x":
                leftend=leftstart+1
            else:
                leftend=0
                co=1
                for i in range(leftstart+1,len(data)):
                    if co==0:
                        leftend=i
                        break
                    elif data[i]=="[":
                        co+=1
                    elif data[i]=="]":
                        co-=1
            #right
            if data[leftend+1]=="x":
                right=None
            else:
                r=data[leftend+1:len(data)-1]  
                right=self.deserialize(r)
             
        return TreeNode(val,self.deserialize(data[leftstart:leftend]),right)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# time complexity o(n)
# space complexity o(n)