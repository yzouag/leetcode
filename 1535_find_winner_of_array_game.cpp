#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        unordered_map<int, int> win_counts;
        int n = arr.size();
        int left = 0;
        int right = 1;

        while (true) {
            if (arr[left] > arr[right]) {
                win_counts[arr[left]] += 1;
                if (win_counts[arr[left]] == k) {
                    return arr[left];
                }
                right += 1;
                if (right >= n) {
                    right = 0;
                    if (left == 0) {
                        right += 1;
                    }
                }
            } else {
                win_counts[arr[right]] += 1;
                if (win_counts[arr[left]] == k) {
                    return arr[left];
                }
                left += 1;
                if (left >= n) {
                    left = 0;
                    if (right == 0) {
                        left += 1;
                    }
                }
            }
        }

        return -1;
    }
};