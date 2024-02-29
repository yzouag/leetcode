#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        unordered_set<string> dic(dictionary.begin(), dictionary.end());

        int n = s.length();
        vector<int> dp(n+1);
        dp[0] = 0;
        for (int i=1; i<n+1; i++) {
            dp[i] = i;
            for (int j=0; j<i; j++) {
                if (dic.find(s.substr(j, i-j)) != dic.end()) {
                    dp[i] = min(dp[i], dp[j]);
                } else {
                    dp[i] = min(dp[i], dp[j]+i-j);
                }
            }
        }
        return dp[n];
    }
};