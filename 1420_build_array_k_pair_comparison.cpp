#include <vector>

using namespace std;

class Solution
{
public:
    using ll = long long;
    static const int N = 55;
    static const int M = 105;
    ll dp[N][M][N];
    ll pre[N][M][N];
    int numOfArrays(int n, int m, int k)
    {
        const int MOD = 1e9 + 7;
        memset(dp, 0, sizeof(dp));
        memset(pre, 0, sizeof(pre));
        for (int elem = 1; elem <= m; elem++)
        {
            dp[1][elem][1] = 1;
            pre[1][elem][1] = elem;
        }
        for (int len = 2; len <= n; len++)
        {
            for (int max_elem = 1; max_elem <= m; max_elem++)
            {
                for (int cost = 1; cost <= k; cost++)
                {
                    // if i want to keep cost
                    dp[len][max_elem][cost] = max_elem * 1LL * dp[len - 1][max_elem][cost]; // there are max_elem ways of adding to end
                    dp[len][max_elem][cost] %= MOD;
                    // if i want to introduce new max element
                    dp[len][max_elem][cost] += pre[len - 1][max_elem - 1][cost - 1];
                    if (dp[len][max_elem][cost] >= MOD)
                        dp[len][max_elem][cost] -= MOD;
                    pre[len][max_elem][cost] = dp[len][max_elem][cost] + pre[len][max_elem - 1][cost];
                    if (pre[len][max_elem][cost] >= MOD)
                        pre[len][max_elem][cost] -= MOD;
                }
            }
        }
        return pre[n][m][k];
    }
};