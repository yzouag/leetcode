#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.length() != word2.length()) {
            return false;
        }

        vector<int> w1_count(26, 0);
        vector<int> w2_count(26, 0);

        for (int i=0; i<word1.length(); i++) {
            w1_count[word1[i]-'a']++;
            w2_count[word2[i]-'a']++;
        }
        
        for (int i=0; i<26; i++) {
            if (w1_count[i] > 0 && w2_count[i] == 0)
                return false;
            if (w2_count[i] > 0 && w1_count[i] == 0)
                return false;
        }

        sort(w1_count.begin(), w1_count.end());
        sort(w2_count.begin(), w2_count.end());
        
        for (int i=0; i<26; i++) {
            if (w1_count[i] != w2_count[i])
                return false;
        }
        return true;
    }
};