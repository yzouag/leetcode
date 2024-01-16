#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minDifficulty(vector<int>& jobDifficulty, int d) {
        int n = jobDifficulty.size();
        if (n < d) {
            return -1;
        }

        vector<vector<int>> dp(n, vector<int>(d+1, -1));
        
        return dfs(0, d, dp, jobDifficulty);
    }

    int dfs(int index, int days_left, vector<vector<int>>& dp, vector<int>& jobDifficulty) {
        if (days_left == 1) {
            return *max_element(jobDifficulty.begin()+index, jobDifficulty.end());
        }

        if (dp[index][days_left] != -1) {
            return dp[index][days_left];
        }

        int res = 9999990;
        int max_dif = 0;
        for (int i=index; i<=jobDifficulty.size()-days_left; i++) {
            max_dif = max(max_dif, jobDifficulty[i]);
            res = min(res, max_dif+dfs(index+1, days_left-1, dp, jobDifficulty));
        }
        dp[index][days_left] = res;
        return res;
    }
};