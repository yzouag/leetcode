#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        priority_queue<int, vector<int>, greater<int>> q;
        for (int i=1; i<heights.size(); i++) {
            if (heights[i] <= heights[i-1])
                continue;
            int diff = heights[i]-heights[i-1];
            if (q.size() < ladders) {
                q.push(diff);
            } else {
                q.push(diff);
                bricks -= q.top();
                if (bricks < 0) {
                    return i-1;
                }
                q.pop();
            }
        }
        return heights.size()-1;
    }
};