#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int max_freq = 0;
        int num_max = 0;

        unordered_map<int, int> freq;
        for (int num: nums) {
            freq[num] += 1;
            if (freq[num] > max_freq) {
                max_freq = freq[num];
                num_max = 1;
            }
            else if (freq[num] == max_freq)
                num_max += 1;
        }

        return max_freq*num_max;
    }
};