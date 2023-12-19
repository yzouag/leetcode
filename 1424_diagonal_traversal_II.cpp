#include <vector>
#include <algorithm>
#include <array>

using namespace std;

bool compare(array<int, 3> a, array<int,3> b) {
    if (a[0]+a[1] > b[0]+b[1]) {
        return true;
    }
    else if (a[0]+a[1] == b[0]+b[1]) {
        return a[0] > b[0];
    }
    return false;
}

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        // int m = nums.size();
        // int n = 0;
        // for (auto row : nums) {
        //     n = max(n, (int)row.size());
        // }
        // vector<int> res;
        // for (int i=0; i<m; i++) {
        //     int k = i;
        //     int j = 0;
        //     while (k>=0 && j < n) {
        //         if (nums[k].size() > j)
        //             res.push_back(nums[k][j]);
        //         k--;
        //         j++;
        //     }
        // }
        // for (int j=1; j<n; j++) {
        //     int k = j;
        //     int i = m-1;
        //     while (k < n && i >= 0) {
        //         if (nums[i].size() > k)
        //             res.push_back(nums[i][k]);
        //         k++;
        //         i--;
        //     }
        // }
        // return res;
        vector<array<int, 3>> elements;
        for (int i=0; i<nums.size(); i++) {
            for (int j=0; j<nums[i].size(); j++) {
                elements.push_back({i, j, nums[i][j]});
            }
        }

        sort(elements.begin(), elements.end(), compare);

        vector<int> res;
        for (auto el : elements) {
            res.push_back(el[2]);
        }
        return res;
    }
};