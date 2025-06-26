# best time to buy and sell stock

prices = [2,7,5,3,2,1]
# Output: 5
def max_profit(prices):
    buy_price = prices[0]
    profit = 0

    for p in prices[1:]:
        print(f'➡ buy_price {buy_price}')
        if buy_price>p:
            buy_price = p
        profit = max(profit, p-buy_price)
        print("profit", profit)
    return profit


res = max_profit(prices)
print('➡ leetcode_121.py:18 res:', res)