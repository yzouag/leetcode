#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int minDeletions(string s) {
        vector<int> counts(26, 0);
        for (auto ch : s) {
            counts[ch-'a'] ++;
        }
        
        unordered_set<int> freqs;
        
        int result = 0;
        for (auto count : counts) {
            while (count != 0 && freqs.find(count) != freqs.end()) {
                count--;
                result += 1;
            }
            freqs.insert(count);
        }
        return result;
    }
};