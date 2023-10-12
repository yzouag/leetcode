#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        vector<int> cost(26);
        for (int i=0; i<26; i++) {
            cost[i] = i+1;
        }
        for (int i=0; i<chars.length(); i++) {
            cost[chars[i]-'a'] = vals[i];
        }

        int curr = 0; 
        int res = 0;
        for (const char& ch : s) {
            curr += cost[ch-'a'];
            if (curr < 0)
                curr = 0;
            else
                res = max(res, curr);
        }
        return res;
    }
};