#include <vector>
#include <algorithm>
#include <random>

using namespace std;

class Solution {
private:
    vector<int> distribution;

public:
    Solution(vector<int>& w) {
        distribution.resize(w.size());
        distribution[0] = w[0];

        for (int i=1; i<w.size(); i++) {
            distribution[i] = distribution[i-1] + w[i];
        }
    }
    
    int pickIndex() {
        int val = rand() % distribution[distribution.size()-1];
        auto upper = upper_bound(distribution.begin(), distribution.end(), val) - distribution.begin();
        return (int)upper;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */