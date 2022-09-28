from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # original post: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
        # denote T[i, k, 0] as the max profit when: prices go to prices[i] (i+1 days), k number of transactions done, 0 stocks hold on hand
        # thus, T[i, k, 1] is max profit of i+1 days, k number of transactions, with 1 stock hold on hand
        # T[0, 0, 0] = 0
        # T[0, 0, 1] = -price[0]
        # T[i, k, 0] = max(T[i-1, k, 0], T[i-1, k, 1] + prices[i] - fee)
        #       T[i-1, k, 0]: do nothing on i+1 day
        #       T[i-1, k, 1] + prices[i]: on this day, sell the stock previous hold
        #       why cannot be T[i-m, k, 1] + prices[i] - fee? Or, why T[i-1, k, 1] >= T[i-m, k, 1]? T[i, k, 1] = max(T[i-1, k, 1], ...) >= T[i-1, k, 1]
        # T[i, k, 1] = max(T[i-1, k, 1], T[i-1, k-1, 0] - prices[i])
        #       T[i-1, k, 1]: do nothing on i+1 day
        #       T[i-1, k-1, 0] - prices[i]: on this day, buy the stock

        # note here we don't need to cache all the 3D T array, since every T_i+1 only derive from T_i, thus we only need to store 2 variables
        # also, since here we can take infinite transactions, the k is never a constrain now, we can ignore it
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash

if __name__ == "__main__":
    prices = [1,3,2,8,4,9]
    fee = 2
    print(Solution().maxProfit(prices, fee))
    # Output: 8
    # The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8

    prices = [1,3,7,5,10,3]
    fee = 3
    print(Solution().maxProfit(prices, fee))
    # Output: 6