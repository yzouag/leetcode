#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<vector<int>> fourSum(vector<int> &nums, int target)
    {
        sort(begin(nums), end(nums));
        return kSum(nums, target, 0, 4);
    }

    vector<vector<int>> kSum(vector<int> &nums, long long target, int start_index, int k)
    {
        if (k == 2)
        {
            return twoSum(nums, target, start_index);
        }

        vector<vector<int>> res;
        for (int i = start_index; i <= nums.size() - k; i++)
        {
            if (i > start_index && nums[i] == nums[i - 1])
                continue;
            auto sub_tuples = kSum(nums, target - nums[i], i + 1, k - 1);
            for (auto &tuple : sub_tuples)
            {
                tuple.push_back(nums[i]);
                res.push_back(tuple);
            }
        }
        return res;
    }

    vector<vector<int>> twoSum(vector<int> &nums, int target, int start)
    {
        vector<vector<int>> res;
        int end = nums.size() - 1;

        while (start < end)
        {
            int sums = nums[start] + nums[end];
            if (sums < target)
            {
                start++;
            }
            else if (sums > target)
            {
                end--;
            }
            else
            {
                vector<int> tuple{nums[start], nums[end]};
                while (nums[start] == tuple[0] && start < end)
                    start++;
                while (nums[end] == tuple[1] && start < end)
                    end--;
                res.push_back(tuple);
            }
        }

        return res;
    }
};
