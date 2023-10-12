# dp[i][j] is number of possible playlists of length i with j unique songs
# base case
# dp[0][0] = 1, 1 playlist of length 0 with 0 songs
# dp[0][not 0] = dp[not 0][0] = 0, 0 playlist of length 0 with multiple unique songs, and 0 playlist of nonzero length with 0 unique songs
# recursion relation:
# - we can add 1 song never played before to every playlist of length i-1 with j-1 unique songs
# - we can also add 1 previous played song from every playlist of length i-1 with j unique songs
# why these two are disjoint?

def numMusicPlaylists(n: int, goal: int, k: int) -> int:
    MOD = 10**9 + 7

    # Initialize the DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(goal + 1)]
    dp[0][0] = 1

    for i in range(1, goal + 1):
        for j in range(1, min(i, n) + 1):
            # The i-th song is a new song
            dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % MOD
            # The i-th song is a song we have played before
            if j > k:
                dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD

    return dp[goal][n]

n = 3
goal = 3
k = 1
print(numMusicPlaylists(n, goal, k))
# Output: 6

n = 2
goal = 3
k = 0
print(numMusicPlaylists(n, goal, k))
# Output: 6

n = 2
goal = 3
k = 1
print(numMusicPlaylists(n, goal, k))
# Output: 2