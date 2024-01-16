#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        // [2, 6, 8, 3, 4, 5, 1]
        // sub1 = [2]
        // sub1 = [2,6]
        // sub1 = [2,6,8]
        // sub1 = [2,6,8], sub2=[2,3]
        // sub1 = [2,6,8], sub2=[2,3,4]
        // sub1 = [2,6,8], sub2=[2,3,4,5]
        // sub1 = [2,6,8], sub2=[2,3,4,5], sub3=[1]

        // instead of keeping different candidates, we can only keep one array and update it every time
        // arr = [2]
        // arr = [2,6]
        // arr = [2,6,8]
        // arr = [2,3,8] # find the smallest one larger than current element, update it
        // arr = [2,3,4]
        // arr = [2,3,4,5]
        // arr = [1,3,4,5]

        vector<int> arr;
        for (int x : nums) {
            if (arr.empty() || arr[arr.size()-1] < x) {
                arr.push_back(x);
            } else {
                auto it = lower_bound(arr.begin(), arr.end(), x);
                *it = x;
            }
        }
        return arr.size();
    }
};