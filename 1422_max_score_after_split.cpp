#include <string>

using namespace std;

class Solution {
public:
    int maxScore(string s) {
        int l = s[0] == '0' ? 1 : 0;
        int r = 0;
        for (int i=1; i<s.length(); i++) {
            if (s[i] == '1')
                r++;
        }

        int result = l+r;
        for (int i=1; i<s.length()-1; i++) {
            if (s[i] == '1')
                r--;
            else
                l++;
            result = max(result, l+r);
        }
        return l+r;
    }
};