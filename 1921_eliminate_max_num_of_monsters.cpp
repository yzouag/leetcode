#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        priority_queue<float, vector<float>, greater<float>> time;
        for (int i=0; i<dist.size(); i++) {
            time.push((float)dist[i] / speed[i]);
        }
        int result = 0;
        while (!time.empty()) {
            if (time.top() > result) {
                time.pop();
                result += 1;
            } else {
                return result;
            }
        }
        return result;
    }
};