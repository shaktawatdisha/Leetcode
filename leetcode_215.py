# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Using min_heap method
import heapq

class Solution:
    def getSecondLargest(self, arr):
        # arr = list(set(arr))  use if it is distinct element
        if len(arr) < 2:
            return -1 
        
        min_heap = []
        heapq.heapify(min_heap)
        
        for i in arr:
            print("before:", min_heap)
            heapq.heappush(min_heap, i) 
            print("mid", min_heap)
            if len(min_heap) > 2:       
                heapq.heappop(min_heap)  
            print("end", min_heap)
            print("-----------------")
        print("Final min_heap:", min_heap)
        
        return min_heap[0] 

if __name__ == "__main__":
    arr = [12, 13, 10, 5, 10, 11, 6] 
    ob = Solution()
    ans = ob.getSecondLargest(arr)
    print(f"The second largest element is: {ans}")
