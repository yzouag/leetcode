#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> counts;

        for (auto num : arr) {
            counts[num]++;
        }

        unordered_set<int> occurs;

        for (auto [_, count] : counts) {
            if (occurs.find(count) != occurs.end())
                return false;
            occurs.insert(count);
        }

        return true;
    }
};