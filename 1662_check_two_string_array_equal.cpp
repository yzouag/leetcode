#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        int s1 = 0;
        int s2 = 0;
        int c1 = 0;
        int c2 = 0;

        while (s1 < word1.size() && s2 < word2.size()) {
            if (c1 < word1[s1].length() && c2 < word2[s2].length()) {
                if (word1[s1][c1] != word2[s2][c2])
                    return false;
                c1++;
                c2++;
            } else {
                if(c1 == word1[s1].length()) {
                    c1 = 0;
                    s1++;
                }
                if(c2 == word2[s2].length()) {
                    c2 = 0;
                    s2++;
                }
            }
        }

        return (s1 == word1.size() && s2 == word2.size());
    }
};