# Merge K Sorted Arrays

# Medium

# Companies:
# Samsung
# Tekion-corp
# Microsoft
# Amazon
# Netflix
# Flipkart
# CRED
# Meesho
# Swiggy
# Dream11
# InMobi
# Oyo

# Problem Statement

# Given K sorted arrays arranged in the form of a matrix of size K*K. The task is to merge them into one sorted array.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 1
# 2
# 3 
# 3 5 9 
# 4 
# 1 2 3 8   
# Sample Output 1:
# 1 2 3 3 5 8 9 
# Explanation Of Sample Input 1:
# After merging the two given arrays/lists [3, 5, 9] and [ 1, 2, 3, 8], the output sorted array will be [1, 2, 3, 3, 5, 8, 9].
# Sample Input 2:
# 1
# 4
# 3
# 1 5 9
# 2
# 45 90
# 5
# 2 6 78 100 234
# 1
# 0
# Sample Output 2:
# 0 1 2 5 6 9 45 78 90 100 234
# Explanation Of Sample Input 2 :
# After merging the given arrays/lists [1, 5, 9], [45, 90], [2, 6, 78, 100, 234] and [0], the output sorted array will be [0, 1, 2, 5, 6, 9, 45, 78, 90, 100, 234].

import heapq
def mergeKSortedArrays(kArrays, k:int):
    heap=[]
    final=[]
    for i in range(len(kArrays)):
        heapq.heappush(heap,(kArrays[i][0],i,0))
    while heap:
        ele,aIndex,eleIndex=heapq.heappop(heap)
        final.append(ele)
        if eleIndex+1<len(kArrays[aIndex]):
            heapq.heappush(heap,(kArrays[aIndex][eleIndex+1],aIndex,eleIndex+1))
    return final

# time complexity: O(nlogk)
# space complexity: O(k)