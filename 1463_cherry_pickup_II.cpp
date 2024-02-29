#include <vector>

using namespace std;

class Solution {
private:
    // dp[r][c1][c2], the max profits when robot1 at [r, c1], robot2 at [r, c2]
    vector<vector<vector<int>>> dp;
    int helper(int row, int c1, int c2, vector<vector<int>>& grid) {
        if (row >= grid.size() || c1 < 0 || c1 >= grid[0].size() || c2 < 0 || c2 >= grid[0].size()) { // base case
            return 0;
        }

        if (dp[row][c1][c2] != -1) // already visited
            return dp[row][c1][c2];

        int profits = 0;
        for (int i=-1; i<=1; i++) {
            for (int j=-1; j<=1; j++) {
                profits = max(profits, helper(row+1, c1+i, c2+j, grid));
            }
        }
        profits = c1 == c2 ? profits + grid[row][c1] : profits + grid[row][c1] + grid[row][c2];
        dp[row][c1][c2] = profits;
        return profits;
    }

public:
    int cherryPickup(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        dp.resize(m, vector<vector<int>>(n, vector<int>(n, -1)));
        return helper(0, 0, n-1, grid);
    }
};