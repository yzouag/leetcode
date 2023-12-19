#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int maxFrequency(vector<int> &nums, int k) {
        sort(nums.begin(), nums.end());
        int left = 0;
        long current_sum = 0;
        for (int right = 0; right < nums.size(); right++) {
            long target = nums[right];
            current_sum += target;

            if ((right-left+1) * target - current_sum > k) {
                current_sum -= nums[left];
                left ++;
            }
        }

        return nums.size() - left;
    }
};