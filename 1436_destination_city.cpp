#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_map<string, bool> has_outgoing;
        for (auto path : paths) {
            has_outgoing[path[0]] = true;
            if (has_outgoing.find(path[1]) == has_outgoing.end()) {
                has_outgoing[path[1]] = false;
            }
        }
        
        for (auto kvpair : has_outgoing) {
            if (kvpair.second == false) {
                return kvpair.first;
            }
        }

        return "";
    }
};