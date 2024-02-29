#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;

        for (int i=0; i<n; i++) {
            res.push_back({nums[i]});
        }

        vector<int>* max_result = &res[0];

        for (int i=1; i<nums.size(); i++) {
            for (int j=0; j<i; j++) {
                if (nums[i] % nums[j] == 0 && res[i].size() < res[j].size()+1){
                    res[i] = res[j];
                    res[i].push_back(nums[i]);
                }
            }
            if (max_result->size() < res[i].size())
                max_result = &res[i];
        }
        return *max_result;
    }
};