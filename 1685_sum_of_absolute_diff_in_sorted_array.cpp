#include <vector>

using namespace std;

class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        vector<int> prefix(nums);
        int n = nums.size();
        for(int i=1; i<n; i++) {
            prefix[i] = prefix[i-1] + prefix[i];
        }

        vector<int> res;
        for(int i=0; i<n; i++) {
            int leftSum = prefix[i] - nums[i];
            int rightSum = prefix[n - 1] - prefix[i];
            
            int leftCount = i;
            int rightCount = n - 1 - i;
            
            int leftTotal = leftCount * nums[i] - leftSum;
            int rightTotal = rightSum - rightCount * nums[i];
            
            res.push_back(leftTotal + rightTotal);        
        }
        return res;
    }
};