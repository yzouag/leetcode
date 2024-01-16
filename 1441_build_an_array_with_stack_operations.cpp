#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        int index = 0;
        vector<string> res;
        for (int i=1; i<=n; i++) {
            if (i != target[index]) {
                res.push_back("Push");
                res.push_back("Pop");
            } else {
                res.push_back("Push");
                index += 1;
                if (index == target.size()) {
                    return res;
                }
            }
        }
        return res;
    }
};