#include <vector>

using namespace std;

// idea: Boyer-Moore majority vote algorithm
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int m1 = 0, m2 = 1, c1 = 0, c2 = 0;
        for (int n : nums) {
            if (m1 == n) c1++;
            else if (m2 == n) c2++;
            else if (c1 == 0) {
                c1 = 1;
                m1 = n;
            }
            else if (c2 == 0) {
                c2 = 1;
                m2 = n;
            }
            else {
                c1 --;
                c2 --;
            }
        }

        c1 = 0;
        c2 = 0;
        for (int n: nums) {
            if (m1 == n)
                c1 ++;
            if (m2 == n)
                c2 ++;
        }

        vector<int> res;
        if (c1 > nums.size()/3)
            res.push_back(m1);
        if (c2 > nums.size()/3 && m1 != m2)
            res.push_back(m2);
        return res;
    }
};