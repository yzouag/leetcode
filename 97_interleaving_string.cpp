#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <functional>

using namespace std;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m = s1.size();
        int n = s2.size();
        int s = s3.size();

        if (s != m + n) {
            return false;
        }

        unordered_map<long long, bool> seen;

        function<bool(int, int)> dp = [&](int i, int j) -> bool {
            // base case
            if (i == m) {
                return s3.substr(s-i-j) == s2.substr(j);
            }
            if (j == n) {
                return s3.substr(s-i-j) == s1.substr(i);
            }

            long long key = static_cast<long long>(i) << 32 | j;  // Combining i and j into a single key
            if (seen.find(key) != seen.end()) {
                return seen[key];
            }

            bool interleavable = false;
            if (s3[i + j] == s1[i]) {
                interleavable |= dp(i + 1, j);
            }
            if (s3[i + j] == s2[j]) {
                interleavable |= dp(i, j + 1);
            }
            seen[key] = interleavable;

            return interleavable;
        };

        return dp(0, 0);
    }
};

int main() {
    // Testing the function
    cout << Solution().isInterleave("abc", "def", "adbcef") << endl; // Expected: true
    cout << Solution().isInterleave("abc", "def", "adbce") << endl;  // Expected: false
    return 0;
}