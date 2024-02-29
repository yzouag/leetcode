#include <vector>

using namespace std;

class Solution {
public:
    int mod = pow(10,9) + 7;
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(maxMove+1, -1)));

        return dfs(startRow, startColumn, maxMove, m, n, dp);
    }

    int dfs(int x, int y, int move, int m, int n, vector<vector<vector<int>>>& dp) {
        if (x < 0 || x >= m || y < 0 || y >= n)
            return 1;
        if (move == 0)
            return 0;
        if (dp[x][y][move] != -1)
            return dp[x][y][move];
        
        long up = dfs(x-1, y, move-1, m, n, dp) % mod;
        long down = dfs(x+1, y, move-1, m, n, dp) % mod;
        long left = dfs(x, y-1, move-1, m, n, dp) % mod;
        long right = dfs(x, y+1, move-1, m, n, dp) % mod;

        int res = (up + down + left + right) % mod;

        dp[x][y][move] = res;

        return dp[x][y][move];
    }
};