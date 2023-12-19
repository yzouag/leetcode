#include <map>
#include <vector>

using namespace std;

class Solution {
public:
    int knightDialer(int n) {
        map<int, vector<int>> previous = {
            {0, {4, 6}},
            {1, {6, 8}},
            {2, {7, 9}},
            {3, {4, 8}},
            {4, {0, 3, 9}},
            {5, {}},
            {6, {0, 1, 7}},
            {7, {2, 6}},
            {8, {1, 3}},
            {9, {2, 4}},
        };

        vector<int> counts(10, 1);
        vector<int> temp(10, 0);
        int mod = 1e9+7;

        for (int i=0; i<n-1; i++) {
            for (int j=0; j<10; j++) {
                temp[j] = 0;
                for (int k : previous[j]) {
                    temp[j] += counts[k];
                    temp[j] %= mod;
                }
            }
            for (int j=0; j<10; j++)
                counts[j] = temp[j];
        }

        int result = 0;
        for (int n : counts) {
            result += n;
            result %= mod;
        }
        return result;
    }
};