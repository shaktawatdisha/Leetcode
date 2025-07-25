# (Greedy Algorithms)
# 134. Gas Station
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

 

# Example 1:

# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.
# Example 2:

# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.


# Solution: 
# Step 1: The key point in solving this problem is that if the total amount of gas is greater than or eaqul to costs, then even if gas runs out midway, starting from a different location will allow a full circuit.
# Step 2: start find the index where we can move forward and gas we can reach to next station


# [1,2,3,4,5](= gas)
# [3,4,5,1,2](= cost)
#    i

# current gas = 0
# start = 1

# current gas = 2 - 4
# Move start point to next.
# Reset current gas to 0.
# ----------------------------------

# [1,2,3,4,5](= gas)
# [3,4,5,1,2](= cost)
#      i

# current gas = 0
# start = 2

# current gas = 3 - 5
# Move start point to next.
# Reset current gas to 0.
# ----------------------------------
# [1,2,3,4,5](= gas)
# [3,4,5,1,2](= cost)
#        i

# current gas = 0
# start = 3

# current gas = 4 - 1
# = 3

# Step 3:  after finding the start point then move forward to loop in circuit



class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1
                
        tank = idx = 0

        for i in range(len(gas)):     
            tank+= gas[i]-cost[i]
            if tank < 0:
                tank, idx = 0, i+1

        return idx 


gas =[5,1,2,3,2]
cost =[4,4,1,5,1]
s = Solution()
res = s.canCompleteCircuit(gas, cost)
print('➡ leetcode_134.py:100 res:', res)