#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> common;
        for (const int& num : nums1) {
            common.insert(num);
        }
        unordered_set<int> res;
        for (const int& num: nums2) {
            if (common.find(num) != common.end())
                res.insert(num);
        }
        return vector<int>{res.begin(), res.end()};
    }
};