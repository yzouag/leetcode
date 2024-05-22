#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;
        for (int i=0; i<n; i++) {
            if (i > 0 && nums[i-1] == nums[i])
                continue;
            
            int target = 0 - nums[i];
            int start = i+1;
            int end = n-1;
            
            while (start < end) {
                int sums = nums[start] + nums[end];
                if (sums < target) {
                    start++;
                } else if (sums > target) {
                    end--;
                } else {
                    res.push_back({nums[i], nums[start], nums[end]});
                    start++;
                    end--;
                    while (nums[start] == nums[start-1] && start < end)
                        start++;
                    while (nums[end] == nums[end+1] && end > start)
                        end--;
                }
            }
        }

        return res;
    }
};