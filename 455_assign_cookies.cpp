#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(s.begin(), s.end(), less<int>());
        sort(g.begin(), g.end(), less<int>());
        int child = 0;
        int cookie = 0;
        while (child < g.size() && cookie < s.size()) {
            if (s[cookie] >= g[child]) {
                child += 1;
            }
            cookie += 1;
        }
        return child;
    }
};