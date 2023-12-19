#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        int dx = abs(sx-fx);
        int dy = abs(sy-fy);

        if (min(dx, dy) + abs(dx-dy) < t) {
            return false;
        }

        if (dx+dy == 0 && t==1) {
            return false;
        }
        
        return true;
    }
};