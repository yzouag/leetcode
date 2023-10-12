# Serve 100 ml of soup A and 0 ml of soup B,
# Serve 75 ml of soup A and 25 ml of soup B,
# Serve 50 ml of soup A and 50 ml of soup B,
# Serve 25 ml of soup A and 75 ml of soup B.

def soupServings(n: int) -> float:
    options = [(100, 0), (75, 25), (50, 50), (25, 75)]
    
    memo = {}
    def recursion(A, B):
        if A <= 0 and B <= 0:
            return 0.5
        if A <= 0 and B > 0:
            return 1
        if A > 0 and B <= 0:
            return 0
        if (A, B) in memo:
            return memo[(A, B)]
        prob = 0
        for op in options:
            prob += 0.25*recursion(A-op[0], B-op[1])
        memo[(A, B)] = prob
        return prob
    return recursion(n, n)

n = 50
print(soupServings(n))
# Output: 0.62500

n = 100
print(soupServings(n))
# Output: 0.71875

# 0.25*1 + 0.25*(0.75+0.125) + 0.25*(0.5+0.125) + 0.25*(0.25+0.125)