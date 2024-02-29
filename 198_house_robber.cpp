#include <vector>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n+2);

        dp[0] = 0;
        dp[1] = 0;
        dp[2] = nums[0];

        int res = 0;

        for (int i=1; i<n; i++) {
            dp[i+2] = nums[i] + max(dp[i], dp[i-1]);
            res = max(res, dp[i+2]);
        }
        return res;
    }
};