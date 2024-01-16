#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums) {
        // unordered_map<int, int> counts;
        // for (int num: nums) {
        //     counts[num]++;
        // }
        // int result = 0;
        // for (auto pair: counts) {
        //     int value = pair.second;
        //     if (value == 1)
        //         return -1;
        //     if (value % 3 == 0)
        //         result += value/3;
        //     else if (value % 3 == 1)
        //         result += 2 + (value-4)/3;
        //     else
        //         result += value/3+1;
        // }
        // return result;

        unordered_map<int, int> counter;
        for (int num : nums) {
            counter[num]++;
        }
        int ans = 0;
        for (auto [_, c]: counter) {
            if (c == 1) {
                return -1;
            }
            ans += ceil((double)(c) / 3);
        }
        return ans;
    }
};