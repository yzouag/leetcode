#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        priority_queue<int, vector<int>, less<int>> pq;
        int total = 0;
        for (auto num : nums) {
            total += num;
            pq.push(num);
        }

        for (int i=0; i<nums.size(); i++) {
            if (total - pq.top() > pq.top())
                return total;
            if (i == 1) {
                return -1;
            }
            total -= pq.top();
            pq.pop();
        }
        return -1;
    }
};