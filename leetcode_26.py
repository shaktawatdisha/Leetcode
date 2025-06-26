# Two pointer refer leetcode solution

def removeDuplicates(nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j+=1
    return j
nums = [1,1,1,1,2]
res = removeDuplicates(nums)
print('➡ number of unique elements in array:', res, nums)