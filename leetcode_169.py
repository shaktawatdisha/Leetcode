# Majority element
# Using hasmap

# variable for major majority
# and Dict for the saving current majority elems


nums = [3,2,3,2]
# Output: 3

def major_elem(nums):
    hash = {}
    majority = res = 0
    for n in nums:
        hash[n] = 1+hash.get(n,0)
        print(f"n {n}, hash[n]: {hash[n]}, majority:{majority}, res:{res}")
        if hash[n]>majority:
            res = n
            majority = hash[n]
         
    return res


res = major_elem(nums)
print('➡ leetcode_169.py:24 res:', res)