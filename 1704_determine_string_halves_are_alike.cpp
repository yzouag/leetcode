#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool halvesAreAlike(string s) {
        int count = 0;
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

        int n = s.length();
        for (int i=n/2; i<n; i++) {
            if (vowels.find(s[i]) != vowels.end()) {
                count++;
            }
            if (vowels.find(s[i-n/2]) != vowels.end()) {
                count--;
            }
        }

        return count == 0;
    }
};