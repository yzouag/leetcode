#include <vector>
#include <algorithm>

using namespace std;

bool comparePoint(vector<int>& lhs, vector<int>& rhs) {
    return lhs[0] < rhs[0];
}

class Solution {
public:

    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), comparePoint);
        int result = 0;
        for (int i=1; i<points.size(); i++) {
            result = max(result, points[i][0] - points[i-1][0]);
        }
        return result;
    }
};