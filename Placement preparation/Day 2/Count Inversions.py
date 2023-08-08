# Count Inversions

# Medium

# Companies:
# Walmart
# Adobe
# Facebook
# Flipkart
# Netflix
# Google
# Amazon
# Tekion-corp
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo
# PayTM

# Problem Statement
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 3
# 3 2 1
# Sample Output 1 :
# 3
# Explanation Of Sample Output 1:
# We have a total of 3 pairs which satisfy the condition of inversion. (3, 2), (2, 1) and (3, 1).
# Sample Input 2 :
# 5
# 2 5 1 3 4
# Sample Output 2 :
# 4
# Explanation Of Sample Output 1:
# We have a total of 4 pairs which satisfy the condition of inversion. (2, 1), (5, 1), (5, 3) and (5, 4).

from os import *

from sys import *

from collections import *

from math import *

from typing import List

 

def merge(arr: List[int], temp: List[int], left: int, mid: int, right: int) -> int:

    inv_count = 0

    i = left

    j = mid

    k = left

    while i <= mid - 1 and j <= right:

        if arr[i] <= arr[j]:

            temp[k] = arr[i]

            k += 1

            i += 1

        else:

            temp[k] = arr[j]

            k += 1

            j += 1

            inv_count += mid - i

    while i <= mid - 1:

        temp[k] = arr[i]

        k += 1

        i += 1

    while j <= right:

        temp[k] = arr[j]

        k += 1

        j += 1

    for i in range(left, right + 1):

        arr[i] = temp[i]

    return inv_count

 

def merge_sort(arr: List[int], temp: List[int], left: int, right: int) -> int:

    inv_count = 0

    if right > left:

        mid = (left + right) // 2

        inv_count += merge_sort(arr, temp, left, mid)

        inv_count += merge_sort(arr, temp, mid + 1, right)

        inv_count += merge(arr, temp, left, mid + 1, right)

    return inv_count

 

# Taking inpit using fast I/O.

def takeInput() :

    n = int(input())

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n

 

# Main.

arr, n = takeInput()

temp = [0] * n

print(merge_sort(arr,temp,0,n-1))


# Time Complexity: O(nlogn)
# Space Complexity: O(n)