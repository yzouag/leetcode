#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string customSortString(string order, string s) {
        vector<int> freqs(26, 0);
        for (const char& c : s) {
            freqs[c-'a']++;
        }
        string res;
        for (const char& c : order) {
            while (freqs[c-'a'] > 0) {
                freqs[c-'a']--;
                res.push_back(c);
            }
        }
        for (int i=0; i<26; i++) {
            while (freqs[i] > 0) {
                freqs[i]--;
                res.push_back('a'+i);
            }
        }
        return res;
    }
};