from typing import List, Tuple
from collections import defaultdict

def change(amount: int, coins: List[int]) -> int:
    # key idea here is
    # use first k coins of all coins
    # then, if use k+1 coin: dp[k+1, amount] = dp[k, amount-coins[k+1]] + dp[k, amount-2*coins[k+1]] + ...
    # or, dp[k+1, amount] = dp[k+1, amount-coins[k+1]] + dp[k, amount]
    dp = [0] * (amount+1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, amount+1):
            dp[j] += dp[j-coin]
    return dp[-1]
    

amount = 5
coins = [1,2,5]
print(change(amount, coins)) # 4

amount = 3
coins = [2]
print(change(amount, coins)) # 0

amount = 10
coins = [10]
print(change(amount, coins)) # 1