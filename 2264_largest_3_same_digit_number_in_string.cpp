#include <string>

using namespace std;

class Solution {
public:
    string largestGoodInteger(string num) {
        int largest = -1;
        string result = "";
        for (int i=0; i<num.length()-2; i++) {
            int temp = stoi(num.substr(i, 3));
            if (temp % 111 == 0 && largest < temp) {
                largest = temp;
                result = num.substr(i,3);
            }
        }
        return result;
    }
};