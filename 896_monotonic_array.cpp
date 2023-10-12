#include <vector>

using namespace std;

class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool not_determined = true;
        bool increase;
        for (int i=0; i < nums.size()-1; i++) {
            if (not_determined) {
                if (nums[i] < nums[i+1]) {
                    not_determined = false;
                    increase = true;
                }
                else if (nums[i] > nums[i+1]) {
                    not_determined = false;
                    increase = false;
                }
            } else {
                if (nums[i] < nums[i+1] && increase == false) {
                    return false;
                }
                else if (nums[i] > nums[i+1] && increase == true) {
                    return false;
                } 
            }
        }
        return true;
    }
};