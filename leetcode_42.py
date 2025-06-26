# 42. Trapping Rain Water
# Hard
# Topics
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


# Solution will be like left and right pointer  and current value finding the maxleft and maxright and subtract the value with maxleft if the value at current posiiton is greater then update the maxleft or maxright also compare the leftmax to rightmax if the value at leftmax is greater then rightmax we will update the rightmax and right pointer compare the rightmax and shifted right pointer and add it to result same algo with leftmax and left pointer add it to the result
# 

height = [0,1,0,2,1,0,1,3,2,1,2,1]
def trap(height):
    l, r = 0, len(height)-1
    maxleft, maxright = height[l], height[r]
    res = 0

    while l<r:
        print("left", l, maxleft)
        print("right", r, maxright)
        if maxleft<maxright:
            l +=1
            maxleft = max(maxleft, height[l])
            res += maxleft-height[l]
        else:
            r-=1
            maxright = max(maxright, height[r])
            res += maxright-height[r]

    return res

res = trap(height)
print('➡ leetcode_42.py:35 res:', res)