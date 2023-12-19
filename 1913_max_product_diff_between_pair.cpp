#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        priority_queue<int, vector<int>, greater<int>> max_heap;
        priority_queue<int, vector<int>, less<int>> min_heap;
        min_heap.push(nums[0]);
        min_heap.push(nums[1]);
        max_heap.push(nums[0]);
        max_heap.push(nums[1]);
        for (int i=2; i<nums.size(); i++) {
            min_heap.push(nums[i]);
            min_heap.pop();
            max_heap.push(nums[i]);
            max_heap.pop();
        }

        int x = min_heap.top();
        min_heap.pop();
        int y = min_heap.top();

        int i = max_heap.top();
        max_heap.pop();
        int j = max_heap.top();

        return i*j-x*y;
    }
};