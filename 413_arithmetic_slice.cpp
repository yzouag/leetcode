#include <vector>

using namespace std;

class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        if (nums.size() < 3) {
            return 0;
        }

        int result = 0;
        for (int i=0; i<nums.size()-2; i++) {
            int diff = nums[i+1]-nums[i];
            int j = i+2;
            while (j < nums.size()) {
                if (nums[j]-nums[j-1] == diff)
                    j += 1;
                else
                    break;
            }
            result += j-i-2;
        }

        return result;
    }
};