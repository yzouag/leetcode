#include<vector>
#include<string>

using namespace std;

class Solution {
public:
    bool makeEqual(vector<string>& words) {
        vector<int> letters(26, 0);

        for (string word : words) {
            for (char l : word) {
                letters[l-'a'] ++;
            }
        }

        for (int i=0; i<26; i++) {
            if (letters[i] % words.size() != 0)
                return false;
        }
        return true;
    }
};