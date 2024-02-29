#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool canCross(vector<int>& stones) {
        if (stones[1] != 1) {
            return false;
        }
        
        unordered_map<int, unordered_set<int>> dp;
        unordered_set<int> stones_dist(stones.begin(), stones.end());

        int size = stones.size();
        int target = stones[size-1];

        dp[1].insert(1);
        for (int i=1; i<size; i++) {
            for (auto step : dp[stones[i]]) {
                for (int j=-1;j<=1; j++) {
                    if (step+j <= 0)
                        continue;
                    int next_stone = stones[i]+step+j;
                    if (next_stone == target)
                        return true;
                    if (stones_dist.find(next_stone) != stones_dist.end()) {
                        dp[next_stone].insert(step+j);
                    }
                }
            }
        }
        return false;
    }
};