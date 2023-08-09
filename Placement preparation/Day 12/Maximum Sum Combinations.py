# Maximum Sum Combinations
# Programming
# Heaps And Maps

# Medium

# Companies:
# Bloomberg
# Adobe
# Samsung
# Oracle
# Amazon
# Microsoft
# Netflix
# Tekion-corp
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM

# Problem Description 

# Given two equally sized 1-D arrays A, B containing N integers each.

# A sum combination is made by adding one element from array A and another element of array B.

# Return the maximum C valid sum combinations from all the possible sum combinations.



# Problem Constraints
# 1 <= N <= 105

# 1 <= A[i] <= 105

# 1 <= C <= N



# Input Format
# First argument is an one-dimensional integer array A of size N.

# Second argument is an one-dimensional integer array B of size N.

# Third argument is an integer C.



# Output Format
# Return a one-dimensional integer array of size C denoting the top C maximum sum combinations.

# NOTE:

# The returned array must be sorted in non-increasing order.



# Example Input
# Input 1:

#  A = [3, 2]
#  B = [1, 4]
#  C = 2
# Input 2:

#  A = [1, 4, 2, 3]
#  B = [2, 5, 1, 6]
#  C = 4


# Example Output
# Output 1:

#  [7, 6]
# Output 1:

#  [10, 9, 9, 8]


# Example Explanation
# Explanation 1:

#  7     (A : 3) + (B : 4)
#  6     (A : 2) + (B : 4)
# Explanation 2:

#  10   (A : 4) + (B : 6)
#  9   (A : 4) + (B : 5)
#  9   (A : 3) + (B : 6)
#  8   (A : 3) + (B : 5)

import heapq
from heapq import heappop,  heappush,heapify
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        A.sort(reverse=True)
        B.sort(reverse=True)
        n= len(A)
        pq= [(-(A[0]+B[0]),(0,0))]
        st=set()
        st.add((0,0))
        ans=[]
        while C>0:
            top= heappop(pq)
            ans.append(top[0]*-1)
            i= top[1][0]
            j= top[1][1]
            if i<n and j<n:
                if (i+1,j) not in st:
                    heappush(pq,(-(A[i+1]+B[j]),(i+1,j)))
                    st.add((i+1,j))
                if (i,j+1) not in st:
                    heappush(pq,(-(A[i]+B[j+1]),(i,j+1)))
                    st.add((i,j+1))
            C-=1
        return ans
    
    # time complexity O(nlogn)
    # space complexity O(n)