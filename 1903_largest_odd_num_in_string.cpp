#include <string>

using namespace std;

class Solution {
public:
    string largestOddNumber(string num) {
        int index;
        for (index=num.size()-1; index >=0; index++) {
            if ((num[index]-'1') % 2 == 0) {
                break;
            }
        }
        return num.substr(0, index+1);
    }
};