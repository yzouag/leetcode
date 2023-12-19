#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    int countPalindromicSubsequence(string s) {
        vector<int> first(26, -1);
        vector<int> last(26, -1);

        for (int i=0; i<s.length(); i++) {
            if (first[s[i]-'a'] == -1) {
                first[s[i]-'a'] = i;
            }
            last[s[i]-'a'] = i;
        }

        int ans = 0;
        for (int i=0; i<26; i++) {
            unordered_set<char> between;
            for (int j=first[i]+1; j<last[i]; j++) {
                between.insert(s[j]);
            }
            ans += between.size();
        }

        return ans;
    }
};