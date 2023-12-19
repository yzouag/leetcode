#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int countNicePairs(vector<int>& nums) {
        unordered_map<int, int> num_count;
        for (int num : nums) {
            string temp = to_string(num);
            reverse(temp.begin(), temp.end());
            int diff = num - stoi(temp);
            if (num_count.find(diff) == num_count.end()) {
                num_count[diff] = 1;
            } else {
                num_count[diff] += 1;
            }
        }

        long result = 0;
        int mod = 1e9+7;
        for (auto const& x : num_count) {
            result += ((long)x.second - 1) * (long)x.second / 2;
            result %= mod;
        }
        return (int)result;
    }
};