# Subset Sums

# Medium

# companies :
# Oracle
# Tekion-corp
# Adobe
# Google
# Flipkart
# Facebook
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo

# Given a list arr of N integers, print sums of all subsets in it.

 

# Example 1:

# Input:
# N = 2
# arr[] = {2, 3}
# Output:
# 0 2 3 5
# Explanation:
# When no elements is taken then Sum = 0.
# When only 2 is taken then Sum = 2.
# When only 3 is taken then Sum = 3.
# When element 2 and 3 are taken then 
# Sum = 2+3 = 5.
# Example 2:

# Input:
# N = 3
# arr = {5, 2, 1}
# Output:
# 0 1 2 3 5 6 7 8
# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function subsetSums() which takes a list/vector and an integer N as an input parameter and return the list/vector of all the subset sums.

# Expected Time Complexity: O(2N)
# Expected Auxiliary Space: O(2N)

# Constraints:
# 1 <= N <= 15
# 0 <= arr[i] <= 104

class Solution:
    #for any element we have two options: can either pick it or not,we will
    #calculate sum across the array using this and append result to answe array
    
    def helper(self,i,n,sumi,arr,ans):
        if i<n:
            self.helper(i+1,n,sumi,arr,ans)#notpicked the element at index i
            self.helper(i+1,n,sumi+arr[i],arr,ans)#picked the element at index i
        else:
            ans.append(sumi)
   
	def subsetSums(self, arr, N):
		# code here
		arr.sort()
		ans=[]
		self.helper(0,N,0,arr,ans)
		return ans

        #time complexity:O(2^n)
        #space complexity:O(2^n)