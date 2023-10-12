#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    // vector<int> searchRange(vector<int> &nums, int target)
    // {
    //     vector<int> res = {-1, -1};
    //     int left = 0;
    //     int right = nums.size() - 1;
    //     int mid;
    //     // first find the left pos
    //     while (left <= right)
    //     {
    //         mid = (right + left) / 2;
    //         if (nums[mid] >= target)
    //             right = mid - 1;
    //         else
    //             left = mid + 1;
    //     }

    //     // cannot find the element return [-1, -1]
    //     if (nums[mid] != target)
    //     {
    //         return res;
    //     }

    //     // find right pos
    //     res[0] = mid;
    //     left = mid;
    //     right = nums.size() - 1;
    //     while (left <= right)
    //     {
    //         mid = (right + left) / 2;
    //         if (nums[mid] > target)
    //             right = mid - 1;
    //         else
    //             left = mid + 1;
    //     }
    //     res[1] = mid;
    //     return res;
    // }

    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        int i = 0;
        int j = n - 1;
        vector<int> ret(2, -1);
        // Search for the left one
        while (i < j)
        {
            int mid = (i + j) /2;
            if (nums[mid] < target) i = mid + 1;
            else j = mid;
        }
        
        if (nums[i]!=target) return ret;
        else ret[0] = i;
        
        // Search for the right one
        j = n-1;  // We don't have to set i to 0 the second time.
        while (i < j)
        {
            int mid = (i + j) /2 + 1;	// Make mid biased to the right
            if (nums[mid] > target) j = mid - 1;  
            else i = mid;				// So that this won't make the search range stuck.
        }
        ret[1] = j;
        return ret; 
    }
};

int main() {
    vector<int> nums = {5,7,7,8,8,10};
    int target = 8;
    vector<int> res = Solution().searchRange(nums, target);
    cout << res[0] << " " << res[1] << endl;
    return 0;
}