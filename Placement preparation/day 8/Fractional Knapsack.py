# Fractional Knapsack

# Medium

# Companies:
# Bloomberg
# Google
# Flipkart
# Samsung
# Adobe
# Walmart
# Amazon
# Facebook
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo

# Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# Note: Unlike 0/1 knapsack, you are allowed to break the item. 

 

# Example 1:

# Input:
# N = 3, W = 50
# values[] = {60,100,120}
# weight[] = {10,20,30}
# Output:
# 240.00
# Explanation:Total maximum value of item
# we can have is 240.00 from the given
# capacity of sack. 
# Example 2:

# Input:
# N = 2, W = 50
# values[] = {60,100}
# weight[] = {10,20}
# Output:
# 160.00
# Explanation:
# Total maximum value of item
# we can have is 160.00 from the given
# capacity of sack.
 

# Your Task :
# Complete the function fractionalKnapsack() that receives maximum capacity , array of structure/class and size n and returns a double value representing the maximum value in knapsack.
# Note: The details of structure/class is defined in the comments above the given function.


# Expected Time Complexity : O(NlogN)
# Expected Auxilliary Space: O(1)


# Constraints:
# 1 <= N <= 105
# 1 <= W <= 105

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    
    #Function to get the maximum total value in the knapsack.
    def fractionalKnapsack(W, arr, n):
        profitByWeight = []
        for i in range(n):
            pbw = arr[i].value / arr[i].weight
            profitByWeight.append((pbw, (arr[i].value, arr[i].weight)))
        profitByWeight.sort()
        profit = 0
        i = n - 1
        while W and i >= 0:
            if profitByWeight[i][1][1] <= W:
                profit += profitByWeight[i][1][0]
                W -= profitByWeight[i][1][1]
                i -= 1
            else:
                profit += profitByWeight[i][0] * W
                i -= 1
                W = 0
        return profit


# time complexity: O(nlogn)
# space complexity: O(n)