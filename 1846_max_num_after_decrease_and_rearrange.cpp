#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        // sort(arr.begin(), arr.end());
        // int prev = 1;
        // for (int i=1; i<arr.size(); i++) {
        //     if (arr[i] >= prev + 1) {
        //         prev = prev+1;
        //     }
        // }
        // return prev;
        
        int n = arr.size();
        vector<int> counts = vector(n + 1, 0);
        
        for (int num : arr) {
            counts[min(num, n)]++;
        }
        
        int ans = 1;
        for (int num = 2; num <= n; num++) {
            ans = min(ans + counts[num], num);
        }
        
        return ans;
    }
};