#  When the game ends, the point is between K and K-1+W
#     What is the probability that the the point is less than N?
#     - If N is greater than K-1+W, probability is 1
#     - If N is less than K, probability is 0
    
#     If W == 3 and we want to find the probability to get a 5
#     - You can get a card with value 1, 2, or 3 with equal probability (1/3)
#     - If you had a 4 and you get a 1: prob(4) * (1/3)
#     - If you had a 3 and you get a 2: prob(3) * (1/3)
#     - If you had a 2 and you get a 3: prob(2) * (1/3)
#     - If you had a 1, you can never reach a 5 in the next draw
#     - prob(5) = prob(4) / 3 + prob(3) / 3 + prob(2) /3
    
#     To generalize:
#     The probability to get point K is
#     p(K) = p(K-1) / W + p(K-2) / W + p(K-3) / W + ... p(K-W) / W
    
#     let wsum = p(K-1) + p(K-2) + ... + p(K-W)
#     p(K) = wsum / W
    
#     dp is storing p(i) for i in [0 ... N]
#     - We need to maintain the window by
#       adding the new p(i), 
#       and getting rid of the old p(i-w)
#     - check i >= W because we would not have negative points before drawing a card
#       For example, we can never get a point of 5 if we drew a card with a value of 6
#     - check i < K because we cannot continue the game after reaching K
#       For example, if K = 21 and W = 10, the eventual point is between 21 and 30
#       To get a point of 27, we can have:
#       - a 20 point with a 7
#       - a 19 point with a 8
#       - a 18 point with a 9
#       - a 17 point with a 10
#       - but cannot have 21 with a 6 or 22 with a 5 because the game already ends

def new21Game(n: int, k: int, maxPts: int) -> float:
    # if k == 0:
    #     return 1
    # memo = {}
    # def dfs(pts_earned):
    #     if pts_earned in memo:
    #         return memo[pts_earned]
    #     lose_prob = 0
    #     if pts_earned + maxPts > n:
    #         lose_prob = (pts_earned+maxPts-n)/maxPts
    #     for i in range(1, maxPts+1):
    #         if pts_earned + i >= k:
    #             break
    #         lose_prob += dfs(pts_earned+i)/maxPts
    #     memo[pts_earned] = lose_prob
    #     return memo[pts_earned]
    # return 1-dfs(0)
    if k == 0 or n >= k + maxPts: 
        return 1
    dp = [1.0] + [0.0] * n
    pts_sum = 1.0
    for i in range(1, n + 1):
        dp[i] = pts_sum / maxPts
        if i < k: 
            pts_sum += dp[i]
        if i - maxPts >= 0: 
            pts_sum -= dp[i - maxPts] # maintain a sliding window
    return sum(dp[k:])

n = 10
k = 1
maxPts = 10
print(new21Game(n, k, maxPts))
# Output: 1.00000

n = 10
k = 2
maxPts = 10
print(new21Game(n, k, maxPts))
# Output: 0.99000

n = 10
k = 3
maxPts = 10
print(new21Game(n, k, maxPts))
# Output: 0.96800

n = 6
k = 1
maxPts = 10
print(new21Game(n, k, maxPts))
# Output: 0.60000

n = 21
k = 17
maxPts = 10
print(new21Game(n, k, maxPts))
# Output: 0.73278