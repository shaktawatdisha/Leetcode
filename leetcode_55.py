# 55. Jump Game
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
# Dynamic programming questions or solve as a greedy algorithm

# Solution: 
# Step1 : starting from the last position if the last value and index can reach to goal 
 
# class Solution:
#     def canJump(self, nums) -> bool:
#         goal = len(nums)-1
#         for i in range(len(nums)-1, -1, -1):
#             print(f"nums[i]+i: {nums[i]+i}    Goal:{goal}")
#             if nums[i] + i >= goal:
#                 goal = i
#         return True if goal==0 else False

# s = Solution()
# nums = [2,3,2,0,1,1]
                
# res = s.canJump(nums)
# print('➡ leetcode_55.py:33 res:', res)





nums = [2,3,1,2,0]
def jump(nums):
    goal = len(nums)-1
    for i in range(len(nums)-1, -1, -1):
        if nums[i]+i >= goal:
            goal=i
    
    return True if goal==0 else False 
res = jump(nums)
print('➡ leetcode_55.py:72 res:', res)