#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int, int> map;
        for (const int &num : nums) {
            if (map.find(num) == map.end()) {
                map[num] = 1;
            }
            else {
                map[num] += 1;
            }
        }
        int res = 0;
        for (auto i=map.begin(); i!=map.end(); i++) {
            res += i->second * (i->second-1) / 2;
        }
        return res;
    }
};
