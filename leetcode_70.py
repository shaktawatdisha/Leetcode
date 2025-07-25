# 70. Climbing Stairs
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Solution : Refer to neetcode youtube channel for the explaination
# Dynamic programming (DP)

def climb(n):
    one, two = 1, 1
    for _ in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one


res = climb(4)
print('➡ leetcode_70.py:36 res:', res)

