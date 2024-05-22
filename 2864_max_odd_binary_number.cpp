#include <string>

using namespace std;

class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int num_ones = 0;
        for (char digit : s) {
            if (digit == '1')
                num_ones++;
        }
        string result(s);
        for (int i=0; i<s.length(); i++) {
            if (num_ones > 1 || i == s.length()-1) {
                result[i] = '1';
                num_ones--;
            } else {
                result[i] = '0';
            }
        }
        return result;
    }
};