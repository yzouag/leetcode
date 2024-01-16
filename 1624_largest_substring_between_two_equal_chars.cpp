#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int n = s.length();
        vector<int> min_index(26, n);
        vector<int> max_index(26, -1);

        int index;
        for (int i=0; i<n; i++) {
            index = s[i] - 'a';
            min_index[index] = min(i, min_index[index]);
            max_index[index] = max(i, max_index[index]);
        }

        int result = -1;
        for (int i=0; i<26; i++) {
            result = max(result, max_index[i]-min_index[i]-1);
        }
        return result;
    }
};