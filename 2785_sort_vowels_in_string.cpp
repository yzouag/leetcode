#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {
public:
    string sortVowels(string s) {
        vector<int> vowels_counts(10, 0);
        unordered_map<char, int> vowel_map({
            {'A', 0},
            {'E', 1},
            {'I', 2},
            {'O', 3},
            {'U', 4},
            {'a', 5},
            {'e', 6},
            {'i', 7},
            {'o', 8},
            {'u', 9}
        });

        for (char c : s) {
            if (vowel_map.find(c) != vowel_map.end()) {
                vowels_counts[vowel_map[c]] += 1;
            }
        }

        string vowels = "AEIOUaeiou";
        int index = 0;
        for (int i=0; i<s.length(); i++) {
            if (vowel_map.find(s[i]) != vowel_map.end()) {
                while (vowels_counts[index] == 0) {
                    index++;
                }
                vowels_counts[index] -= 1;
                s[i] = vowels[index];
            }
        }
        return s;
    }
};