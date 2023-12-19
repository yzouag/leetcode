#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int result = 0;
        int current_level = 0;
        for (int i=1; i<nums.size(); i++) {
            if (nums[i] > nums[i-1]) {
                current_level ++;
            }
            result += current_level;
        }
        return result;
    }
};