#include <vector>

using namespace std;

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> pos;
        vector<int> neg;
        for (int num : nums) {
            if (num > 0)
                pos.push_back(num);
            else
                neg.push_back(num);
        }
        vector<int> res(nums.size());

        for (int i=0; i<nums.size();i++) {
            if (i%2 == 0)
                res[i] = pos[i/2];
            else
                res[i] = neg[i/2];
        }
        return res;
    }
};