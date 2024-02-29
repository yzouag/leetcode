#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<int> dp(matrix[0].begin(), matrix[0].end());
        vector<int> temp(n);
        for (int i=1; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (j==0)
                    temp[j] = min(dp[0], dp[1]) + matrix[i][j];
                else if (j==n-1)
                    temp[j] = min(dp[n-1], dp[n-2]) + matrix[i][j];
                else
                    temp[j] = min(min(dp[j], dp[j+1]), dp[j-1]) + matrix[i][j];
            }
            copy(temp.begin(), temp.end(), dp.begin());
        }
        return *min_element(dp.begin(), dp.end());
    }
};