#include <vector>

using namespace std;

class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        int lower_bound = floor(log10(low)) + 1;
        int upper_bound = floor(log10(high)) + 1;

        vector<int> res;
        for (int k=lower_bound; k<=upper_bound; k++) {
            for (int i=1; i<=9-k+1; i++) {
                int number = 0;
                for (int j=0; j<k; j++) {
                    number += (i+j)*pow(10, k-j-1);
                }

                if (number >= low) {
                    if (number > high) {
                        return res;
                    }
                    res.push_back(number);
                }
            }
        }
        return res;
    }
};