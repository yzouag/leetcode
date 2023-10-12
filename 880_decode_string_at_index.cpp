#include <string>

using namespace std;

class Solution {
public:
    string decodeAtIndex(string s, int k) {
        int N = 0;
        int current_ch_ind;
        for (current_ch_ind=0; N<k; current_ch_ind++)
            N = isdigit(s[current_ch_ind]) ? N * (s[current_ch_ind] - '0') : N+1;
        // now N >= k
        while (current_ch_ind--) {
            // 'ab2cd3e5'
            // if current_ch_ind point to 3, then current N is 18
            // say k is 14, it is same as only 'ababcd', k is 2
            if (isdigit(s[current_ch_ind])) {
                N /= s[current_ch_ind] - '0';
                k %= N;
            }
            else {
                N -= 1;
                if (k % N == 0) {
                    return string(1, s[current_ch_ind]);
                }
            }
        }
        return "";
    }
};