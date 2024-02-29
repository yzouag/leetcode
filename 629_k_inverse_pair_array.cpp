#include <vector>

using namespace std;

// if we have [1..4] already calculated
// for any permutation x x x x, we add 5 to the list
// 5 x x x x (we will have 4 more inverse pairs)
// x 5 x x x (we will have 3 more inverse pairs)
// f(n, k) is the array of size n with k inverse pairs
// f(n, k) = f(n-1, k)        + f(n-1, k-1)    + ... + f(n-1, k-n+1)
//          put n at the end  put n at 2nd last       put n at 1st pos
//
// we further optimize this recursive relationship:
// f(n, k) = f(n-1, k) + f(n-1, k-1) + f(n-1, k-2) + ... + f(n-1, k-n+1) --->(1)
// f(n, k-1) = f(n-1, k-1) + f(n-1, k-2) + f(n-1, k-3) + ... + f(n-1, k-n+1)+ f(n-1, k-n) --->(2)
// subtract eqn 2 from eqn 1,we get
// f(n, k) = f(n, k-1) + f(n-1, k) - f(n-1, k-n)
class Solution {
private:
    const int mod=int(1e9+7);
public:
    int kInversePairs(int n, int k) {
        vector<int> prev(k+1,0),curr(k+1,0);
        prev[0]=curr[0]=1;
        for(int N=1;N<=n;++N) {
            for(int K=0;K<=k;++K) {
                curr[K] = (prev[K] + (K > 0 ? curr[K - 1] : 0)) % mod;
                curr[K] = (curr[K] + mod - (K >= N ? prev[K-N] : 0)) % mod;
            }
            prev = curr;
        }
        return curr[k];
    }
};