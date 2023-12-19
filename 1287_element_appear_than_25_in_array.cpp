#include <vector>

using namespace std;

class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int total = arr.size();
        int count = 1;
        for (int i=1; i<total; i++) {
            if (arr[i] == arr[i-1]) {
                count += 1;
                if (count > total/4) {
                    return arr[i];
                }
            } else {
                count = 1;
            }
        }
        return arr[0];
    }
};