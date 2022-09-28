from typing import List
def maxProfit(prices: List[int]) -> int:
    prev_cash, cash, hold = 0, 0, -prices[0]
    for i in range(1, len(prices)):
        cur_cash = cash
        cash = max(cur_cash, hold + prices[i])
        hold = max(hold, prev_cash - prices[i])
        prev_cash = cur_cash
    return cash

prices = [1,2,3,0,2]
print(maxProfit(prices))
# Output: 3

prices = [1]
print(maxProfit(prices))
# Output: 0
