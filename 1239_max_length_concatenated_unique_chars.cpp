#include <vector>
#include <string>
#include <bitset>

using namespace std;

class Solution {
public:
    int maxLength(vector<string>& arr) {
        vector<bitset<26>> arr_mask = {bitset<26>()};
        
        int res = 0;
        for (auto str : arr) {
            bitset<26> mask;
            for (auto ch : str)
                mask.set(ch-'a');
            if (mask.count() != str.size())
                continue;
                
            int current_candidate_counts = arr_mask.size();
            for (int i=0; i<current_candidate_counts; i++) {
                if ((arr_mask[i] & mask).any())
                    continue;
                arr_mask.push_back(arr_mask[i] | mask);
                res = max(res, (int)arr_mask[i].count() + (int)mask.count());
            }
        }
        
        return res;
    }
};