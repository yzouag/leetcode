from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    # c[n] = 1 + min(c[n-coins[0]], c[n-coins[1]], ...)
    c = [0] * (amount+1)
    for i in range(1, amount+1):
        minimum = 10001
        for coin in coins:
            if i - coin < 0 or c[i-coin] == -1:
                continue
            else:
                minimum = min(minimum, c[i-coin])
        c[i] = 1 + minimum if minimum != 10001 else -1
    return c[-1]

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount)) # Output: 3

coins = [2]
amount = 3
print(coinChange(coins, amount)) # Output: -1

coins = [1]
amount = 0
print(coinChange(coins, amount)) # Output: 0