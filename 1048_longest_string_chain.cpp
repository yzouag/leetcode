#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(), [](const string &a, const string &b){
            a.size() < b.size();
        });
        int res = 0;
        unordered_map<string, int> dp;
        for (const string &word : words)
        {
            for (int i=0; i<word.size(); i++) {
                string pre = word.substr(0, i) + word.substr(i+1);
                dp[word] = max(dp[word], dp.find(pre)==dp.end() ? 1 : dp[pre]+1);
            }
            res = max(res, dp[word]);
        }
        return res;
    }
};