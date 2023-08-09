# Minimum Spanning Tree

# Medium

# Given a weighted, undirected and connected graph of V vertices and E edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.

 

# Example 1:

# Input:
# 3 3
# 0 1 5
# 1 2 3
# 0 2 1

# Output:
# 4
# Explanation:

# The Spanning Tree resulting in a weight
# of 4 is shown above.
# Example 2:

# Input:
# 2 1
# 0 1 5

# Output:
# 5
# Explanation:
# Only one Spanning Tree is possible
# which has a weight of 5.
 

# Your task:
# Since this is a functional problem you don't have to worry about input, you just have to complete the function spanningTree() which takes a number of vertices V and an adjacency list adj as input parameters and returns an integer denoting the sum of weights of the edges of the Minimum Spanning Tree. Here adj[i] contains vectors of size 2, where the first integer in that vector denotes the end of the edge and the second integer denotes the edge weight.
 

# Constraints:
# 2 ≤ V ≤ 1000
# V-1 ≤ E ≤ (V*(V-1))/2
# 1 ≤ w ≤ 1000
# The graph is connected and doesn't contain self-loops & multiple edges.

class Solution:
    def spanningTree(self, V, adj):
        #code here
        key=[float('inf')]*V
        mst=[False]*V
        parent=[-1]*V
        key[0]=0
        parent[0]=-1
        for i in range(V):
            mini=float('inf')
            u=0
            for v in range(V):
                if mst[v]==False and key[v]<mini:
                    u=v
                    mini=key[v]
                    
            mst[u]=True
            for neighbor, weight in adj[u]:
                v= neighbor
                w=weight
                if mst[v]==False and w<key[v]:
                    parent[v]=u
                    key[v]=w
        return sum(key)
    

    # time complexity: O(V^2)
    # space complexity: O(V)