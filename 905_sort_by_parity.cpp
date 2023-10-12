#include <vector>

using namespace std;

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int i = 0;
        int j = nums.size()-1;
        while (i < j) {
            if (nums[i] % 2 == 0) {
                i += 1;
            } else {
                swap(nums[i], nums[j]);
                j -= 1;
            }
        }
        return nums;
    }
};