#  two sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums, target):
    num_dict = {}
    for i in range(len(nums)):
        target_value = target-nums[i]
        if target_value in num_dict:
            return [i, num_dict[target_value]]
        num_dict[nums[i]]=i
    return []

nums = [2,7,11,15]
target = 9
twoSum(nums, target)