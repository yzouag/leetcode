#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        unordered_map<char, int> map;
        for (char ch : chars) {
            if (map.find(ch) == map.end()) {
                map[ch] = 1;
            } else {
                map[ch] += 1;
            }
        }

        int result = 0;
        for (string word : words) {
            unordered_map<char, int> copy(map);
            bool valid = true;
            for (char ch : word) {
                if (copy.find(ch) == map.end()) {
                    valid = false;
                    break;
                }
                copy[ch] -= 1;
                if (copy[ch] < 0) {
                    valid = false;
                    break;
                }
            }
            if (valid)
                result += word.length();
        }

        return result;
    }
};