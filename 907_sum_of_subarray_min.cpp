#include <vector>
#include <algorithm>
#include <set>

using namespace std;

// [3 1 5]
// [1 1]
// [1]

// [3 1 5 2]
// [1 1 2]
// [1 1]
// [1]

// [3 1 5 2 4]
// [1 1 2 2]
// [1 1 2]
// [1 1]
// [1]

// add 4 to the [3 1 5 2]
// we add 4, 2, 2, 1, 1 to the result

// add 2 to [3 1 5]
// we add 2, 2, 1, 1 to the result

// so, if we add 1 to [3 1 5 2 4], what would happen?
// we add 1, 1, 1, 1, 1, 1 to the result
class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        long mod = 1e9 + 7, ans = 0, n = arr.size();
        vector<vector<int>> v;
        for (int i = 0; i < n; i++)
            v.push_back({arr[i], i});

        auto cnt = [&](long x){ return x * (x + 1) / 2; };
        sort(v.begin(), v.end());
        set<int> st = {-1, (int)n};
        for (auto &a : v)
        {
            auto it = st.upper_bound(a[1]);
            long l = *prev(it) + 1, r = *it - 1;
            long m = r - l + 1, left = a[1] - l, right = r - a[1];
            long x = cnt(m) - (cnt(left) + cnt(right));
            st.insert(a[1]);
            ans = (ans + ((x * a[0]) % mod)) % mod;
        }
        return ans % mod;
    }
};