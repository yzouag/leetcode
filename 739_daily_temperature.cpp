#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> st;
        int size = temperatures.size();
        st.push({-1, size});

        vector<int> res(size, 0);

        for (int i=1; i<=size; i++) {
            int temp = temperatures[size-i];
            while (!st.empty() && st.top().first <= temp) {
                st.pop();
            }
            if (!st.empty()) {
                res[size-i] = st.top().second - (size-i);
            }
            st.push({temp, size-i});
        }
        return res;
    }
};