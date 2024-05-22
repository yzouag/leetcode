#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(), tokens.end());

        int required_power = 0;
        for (int& token : tokens) {
            required_power += token;
        }

        int n = tokens.size();
        int l = 0;
        int r = n-1;

        int max_score = 0;
        while (power >= tokens[l] || l - (n-1-r) > 0) {
            if (power >= required_power) {
                max_score = max(r - (n-r) + 2, max_score);
            }
            if (power >= tokens[l]) {
                required_power -= tokens[l];
                power -= tokens[l];
                l++;
            } else {
                required_power -= tokens[r];
                power += tokens[r];
                r--;
            }
            max_score = max(max_score, l - (n-1-r));
            if (l > r)
                break;
        }
        return max_score;
    }
};