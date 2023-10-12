#include <vector>
#include <functional>

using namespace std;

class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int l1 = nums1.size();
        int l2 = nums2.size();

        vector<vector<int>> memo(l1, vector<int>(l2, 0));

        function<int(const int&, const int&)> dp = [&](const int& i, const int& j) {
            if (memo[i][j] != 0) {
                return memo[i][j];
            }
            if (i == l1-1 && j == l2-1) {
                return nums1[i] * nums2[j];
            }
            if (i == l1-1)
                memo[i][j] = max(nums1[i]*nums2[j], dp(i, j+1));
            else if (j == l2-1)
                memo[i][j] = max(nums1[i]*nums2[j], dp(i+1, j));
            else 
                memo[i][j] = max(nums1[i]*nums2[j]+dp(i+1, j+1), max(dp(i, j+1), dp(i+1, j)));
            return memo[i][j];
        };

        return dp(0,0);
    }
};