from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        difference = [0] * (len(prices) - 1)
        for i in range(len(difference)):
            difference[i] = prices[i+1] - prices[i]
        max_profit = 0
        current_max_profit = 0
        for profit in difference:
            current_max_profit = current_max_profit + profit
            if current_max_profit > max_profit:
                max_profit = current_max_profit
            if current_max_profit < 0:
                current_max_profit = 0
        return max_profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    assert Solution().maxProfit(prices) == 5

    prices = [7,6,4,3,1]
    assert Solution().maxProfit(prices) == 0
