#include <string>

using namespace std;

// 111110
// 11110 -> 
// 110101011
class Solution {
public:
    int minOperations(string s) {
        int zero_first = 0;
        int one_first = 0;
        for (int i=0; i<s.length(); i++) {
            if (i%2==0) {
                if (s[i] == '0') {
                    one_first += 1;
                } else {
                    zero_first += 1;
                }
            } else {
                if (s[i] == '0') {
                    zero_first += 1;
                } else {
                    one_first += 1;
                }
            }
        }
        return min(zero_first, one_first);
    }
};