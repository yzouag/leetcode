#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        unordered_map<int, int> counts;
        for (auto num: nums) {
            counts[num] ++;
        }
        
        int max_count = 0;
        for (auto [_, c] : counts) {
            if (c > max_count)
                max_count = c;
        }

        vector<vector<int>> result(max_count, vector<int>());
        for (auto [n, c] : counts) {
            for (int i=0; i<c; i++) {
                result[i].push_back(n);
            }
        }
        return result;
    }
};