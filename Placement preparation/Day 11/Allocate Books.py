# Allocate Books
# Programming
# Binary Search

# Medium

# Companies:
# Microsoft
# Google
# Walmart
# Samsung
# Netflix
# Flipkart
# Adobe
# Amazon
# Tekion-corp
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM
# Byju's

# Problem Description

# Given an array of integers A of size N and an integer B.

# The College library has N books. The ith book has A[i] number of pages.

# You have to allocate books to B number of students so that the maximum number of pages allocated to a student is minimum.

# A book will be allocated to exactly one student.
# Each student has to be allocated at least one book.
# Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
# Calculate and return that minimum possible number.

# NOTE: Return -1 if a valid assignment is not possible.



# Problem Constraints
# 1 <= N <= 105
#  1 <= A[i], B <= 105



# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer B.



# Output Format
# Return that minimum possible number.



# Example Input
# Input 1:
# A = [12, 34, 67, 90]
# B = 2
# Input 2:
# A = [5, 17, 100, 11]
# B = 4


# Example Output
# Output 1:
# 113
# Output 2:
# 100


# Example Explanation
# Explanation 1:
# There are two students. Books can be distributed in following fashion : 
# 1)  [12] and [34, 67, 90]
#     Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
# 2)  [12, 34] and [67, 90]
#     Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
# 3)  [12, 34, 67] and [90]
#     Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages
#     Of the 3 cases, Option 3 has the minimum pages = 113.

def findPages(arr, N, M):
    #code here
    if(M>N):
        return(-1)
    s=0
    sum=0
    for i in range(N):
        sum+=arr[i]
    e=sum
    ans=-1
    mid=s+(e-s)//2
    while(s<=e):
        if(ispossible(arr,N,M,mid)):
            ans=mid
            e=mid-1
        else:
            s=mid+1
        mid=s+(e-s)//2
    return(ans)
       
def ispossible(arr,N,M,mid):
    studentcount=1
    pagesum=0
    for i in range(N):
        if(pagesum+arr[i]<=mid):
            pagesum+=arr[i]
        else:
            studentcount+=1
            if(studentcount>M or arr[i]>mid):
                return False
            pagesum=arr[i]
    return True
   
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        arr=A
        M=B
        N=len(A)
        return(findPages(arr,N,M))
    
    # time complexity: O(n log n)
    # space complexity: O(1)