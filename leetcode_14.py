# 14. Longest Common Prefix
# Solved
# Easy
# Topics
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.



def longestCommonPrefix(strs):
    pref = ''
    for i in range(len(strs[0])):
        print('➡ leetcode_14.py:25 i:', i)
        for j in strs:
            print('➡ leetcode_14.py:27 j:', j)
            if i>=len(j) or j[i]!=strs[0][i]:
                return pref
        pref+=strs[0][i]
    return pref


res = longestCommonPrefix(strs = ["flower","flow","floght"])
print('➡ leetcode_14.py:33 res:', res)

