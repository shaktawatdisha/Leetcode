# 53. Maximum Subarray
# Medium
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

nums =[-2,1,-3,4,-1,2,1,-5,4]
def max_sub(nums):
    maxsub = nums[0]
    cursum = 0

    for n in nums:
        # print('➡ leetcode_53.py:31 i:', n)
        if cursum<0:
            cursum = 0
        cursum += n
        print('➡ cursum:', cursum)
        maxsub = max(cursum, maxsub)
        print("➡ maxsub",maxsub)
    return maxsub

res = max_sub(nums)
print('➡ leetcode_53.py:30 res:', res)
    
