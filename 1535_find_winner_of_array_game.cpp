#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        // no need to consider who is 0 who is 1, only count how many terms a number can stay
        int curr = arr[0];
        int counts = 0;

        for (int i=1; i<arr.size(); i++) {
            if (curr < arr[i]) {
                curr = arr[i];
                counts = 0;
            }
            if (++counts == k)
                return curr;
        }

        // if after one loop, no one is larger than k. current number will be the largest number
        // and in the second loop, it will never change
        return curr;
    }
};