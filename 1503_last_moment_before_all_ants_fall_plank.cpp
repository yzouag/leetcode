#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        if (left.size() == 0 && right.size() == 0) {
            return 0;
        }
        if (right.size() == 0) {
            return *max_element(left.begin(), left.end());
        }
        if (left.size() == 0) {
            return n-*min_element(right.begin(), right.end());
        }
        return max(n-*min_element(right.begin(), right.end()), *max_element(left.begin(), left.end()));
    }
};