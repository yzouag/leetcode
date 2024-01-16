#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int minSteps(string s, string t) {
        vector<int> s_count(26, 0);
        vector<int> t_count(26, 0);
        
        int n = s.length();

        for (int i=0; i<n; i++) {
            s_count[s[i]-'a']++;
            t_count[t[i]-'a']++;
        }

        int res = 0;

        for (int i=0; i<26; i++) {
            if (t_count[i] > s_count[i]) {
                res += t_count[i] - s_count[i];
            }
        }

        return res;
    }
};