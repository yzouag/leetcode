#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        int start = 0;
        while (start < words.size()) {
            // put one word in this new line
            int width = words[start].size();
            int end = start + 1;
            
            // check how many more we can put
            while (end < words.size()) {
                int new_width = width + words[end].size() + 1; // +1 for space between two words
                if (new_width > maxWidth) 
                    break;
                width = new_width;
                ++end;
            }

            // now pack all words from start to end into a line
            string& line = res.emplace_back();
            int count = end - start;
            line.append(words[start]); // put the first word

            int extra_space_per_gap = 0;
            int one_more_space_gaps = 0; // for different gap, the space is different
            // if last line, append a lot of space until end
            // else do regular
            if (count > 1 && end < words.size()) { // not last line and not single word
                int gap = count-1;
                int extra_space = maxWidth - width;
                extra_space_per_gap = extra_space / gap;
                one_more_space_gaps = extra_space % gap;
            }
            for (int i = 1; i < count; i++) {
                int space_count = 1 + extra_space_per_gap + (one_more_space_gaps-- > 0);
                line.resize(line.size() + space_count, ' ');
                line.append(words[start + i]);
            }
            line.resize(maxWidth, ' ');
            start = end;
        }
        return res;
    }
};