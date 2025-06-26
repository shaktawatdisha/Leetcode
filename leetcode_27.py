nums = [3,2,2,3,7]
val = 7
# Output: 2, nums = [2,2,_,_]

def remove_val(nums, val):
    k = 0 
    for i in range(len(nums)):
        if val != nums[i]:
            nums[k]=nums[i]
            k+=1
    return k


res = remove_val(nums, val)
print('➡ leetcode_27.py:14 res:', res)
