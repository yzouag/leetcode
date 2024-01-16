#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map<int, int> loss_counts;
        for (auto match : matches) {
            loss_counts[match[1]]++;
        }
        vector<vector<int>> res(2, vector<int>());

        unordered_set<int> all_win;

        for (auto match : matches) {
            if (loss_counts.find(match[0]) == loss_counts.end()) {
                all_win.insert(match[0]);
            }
        }

        for (int i : all_win) {
            res[0].push_back(i);
        }

        for (auto pair : loss_counts) {
            if (pair.second == 1)
                res[1].push_back(pair.first);
        }

        sort(res[0].begin(), res[0].end());
        sort(res[1].begin(), res[1].end());

        return res;
    }
};