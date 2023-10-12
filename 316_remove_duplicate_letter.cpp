#include <string>
#include <array>
#include <stack>

using namespace std;

class Solution {
public:
    string removeDuplicateLetters(string s) {
        array<int, 26> last_occ;
        array<bool, 26> in_result{};
        
        for (int i=0; i<s.length(); i++)
            last_occ[s[i] - 'a'] = i;

        string res = "";
        for (int i=0; i<s.length(); i++) {
            if (!in_result[s[i]-'a']) {
                while (res.length() > 0 && res.back() > s[i] && last_occ[res.back()-'a'] > i) {
                    in_result[res.back()-'a'] = false;
                    res.pop_back();
                }

                res += s[i];
                in_result[s[i]-'a'] = true;
            }
        }

        return res;
    }
};