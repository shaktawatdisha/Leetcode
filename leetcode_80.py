# two pointer question refer leetcode solutions for this approach

nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]

def removeduplicates(nums):
    k=2
    for i in range(2, len(nums)):
        if nums[i] != nums[k-2]:
            nums[k]=nums[i]
            k+=1
    return k

res = removeduplicates(nums)
print('➡ leetcode_80.py:14 res:', res)
