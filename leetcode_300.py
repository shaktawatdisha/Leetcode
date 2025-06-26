# 300. Longest Increasing Subsequence
# Medium
# Topics
# Companies
# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1


def LengthofLIS(nums):
    dp = [1] * len(nums)
    print("dp:",dp)
    for i in range(len(nums), -1, -1):
        for j in range(i+1, len(nums)):
            print(nums[i], nums[j])
            if nums[i]<nums[j]:
                dp[i] = max(dp[i],1+dp[j])
    return max(dp)


nums = [10,9,2,5,3,7,101,18]
res = LengthofLIS(nums)
print('➡ leetcode_300.py:29 res:', res)