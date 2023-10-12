# denote dp[i, j] as num of operations to change s[i,j] to target string
# another observation:
# to change s[i,j] to target string, the optimal way is always 
def strangePrinter(s: str) -> int:
    

s = "aaabbb"
print(strangePrinter(s))
# Output: 2

s = "aba"
print(strangePrinter(s))
# Output: 2