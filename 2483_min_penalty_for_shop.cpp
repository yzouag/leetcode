#include <string>

using namespace std;

class Solution {
public:
    int bestClosingTime(string customers) {
        // int n = 0;
        // int length = customers.length();
        // for (int i=0; i<length; i++) {
        //     if (customers[i] == 'N')
        //         n++;
        // }

        int curr_penal = 0;
        int min_penal = curr_penal;
        int min_day = 0;
        for (int i=0; i<customers.length(); i++) {
            if (customers[i] == 'Y')
                curr_penal -= 1;
            else
                curr_penal += 1;
            if (curr_penal < min_penal) {
                min_penal = curr_penal;
                min_day = i+1;
            }
        }
        return min_day;
    }
};