#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        vector<vector<int>> res;

        unordered_map<int, vector<int>> size_nums;
        for (int i=0; i<groupSizes.size(); i++) {
            size_nums[groupSizes[i]].push_back(i);
        }

        for (auto [size, nums] : size_nums) {
            for (int i=0; i<nums.size(); i+=size) {
                res.emplace_back(nums.begin()+i, nums.begin()+i+size);
            }
        }
        return res;
    }
};