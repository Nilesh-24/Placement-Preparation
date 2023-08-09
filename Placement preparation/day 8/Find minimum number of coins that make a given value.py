# Given a value V, if we want to make a change for V cents, and we have an infinite supply of each of C = { C1, C2, .., Cm} valued coins, what is the minimum number of coins to make the change? If it’s not possible to make a change, print -1.

#companies:
# Flipkart
# Tekion-corp
# Facebook
# Bloomberg
# Amazon
# Walmart
# Adobe
# Google
# Microsoft
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM

# Examples:  

# Input: coins[] = {25, 10, 5}, V = 30
# Output: Minimum 2 coins required We can use one coin of 25 cents and one of 5 cents 

# Input: coins[] = {9, 6, 5, 1}, V = 11
# Output: Minimum 2 coins required We can use one coin of 6 cents and 1 coin of 5 cents


# This problem is a variation of the problem discussed Coin Change Problem. Here instead of finding the total number of possible solutions, we need to find the solution with the minimum number of coins.

# The minimum number of coins for a value V can be computed using the below recursive formula. 

# If V == 0, then 0 coins required.
# If V > 0
#    minCoins(coins[0..m-1], V) = min {1 + minCoins(V-coin[i])} 
#                                where i varies from 0 to m-1 
#                                and coin[i] <= V


import sys

def minCoins(coins, m, V):

	# base case
	if (V == 0):
		return 0

	# Initialize result
	res = sys.maxsize
	
	# Try every coin that has smaller value than V
	for i in range(0, m):
		if (coins[i] <= V):
			sub_res = minCoins(coins, m, V-coins[i])

			# Check for INT_MAX to avoid overflow and see if
			# result can minimized
			if (sub_res != sys.maxsize and sub_res + 1 < res):
				res = sub_res + 1

	return res

# Driver program to test above function
coins = [9, 6, 5, 1]
m = len(coins)
V = 11
print("Minimum coins required is",minCoins(coins, m, V))

# time complexity: O(mV)
# space complexity: O(V)