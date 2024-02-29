#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        unordered_map<int, int> dp;
        return dfs(0, dp, k, arr);
    }

    int dfs(int i, unordered_map<int, int>& dp, int k, vector<int>& arr) {
        if (dp.find(i) != dp.end()) {
            return dp[i];
        }
        int max_res = 0;
        int curr_max = 0;
        for (int j=1; j<=k; j++) {
            if (i+j-1 >= arr.size()) {
                break;
            }
            curr_max = max(curr_max, arr[i+j-1]);
            max_res = max(max_res, dfs(i+j, dp, k, arr)+curr_max*j);
        }
        dp[i] = max_res;
        return max_res;
    }
};