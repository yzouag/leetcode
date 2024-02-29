#include <vector>
#include <string>

using namespace std;

class Solution {
private:
    bool compareString(string word) {
        int start = 0;
            int end = word.length()-1;
            while (start < end) {
                if (word[start] != word[end]) {
                    return false;
                }
                start++;
                end--;
            }
        return true;
    }
public:
    string firstPalindrome(vector<string>& words) {
        for (string word : words) {
            if (compareString(word))
                return word;
        }
        return "";
    }
};