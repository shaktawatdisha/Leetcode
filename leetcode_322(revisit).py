# 322. Coin Change
# Medium
# Topics
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0


# Solution: this is dynamic programming question which is solved by 

def coin_change(coins, amount):
    dp = [amount+1] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
            print('dp',dp)
            print(f'➡ x:{x}, coinn:{coin}, dp[x]:{dp[x]}, dp[x - coin]:{dp[x - coin]}')

    return dp[amount] if dp[amount] != float('inf') else -1


coins = [1,3,4,5]
amount = 7
res = coin_change(coins, amount)
print('➡ leetcode_322.py:42 res:', res)