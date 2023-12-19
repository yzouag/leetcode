#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        priority_queue<int, vector<int>, greater<int>> queue;

        queue.push(nums[0]);
        queue.push(nums[1]);

        for (int i=2; i<nums.size(); i++) {
            queue.push(nums[i]);
            queue.pop();
        }

        int x = queue.top() - 1;
        queue.pop();
        int y = queue.top() - 1;
        return x*y;
    }
};