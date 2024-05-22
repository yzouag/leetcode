#include <string>
#include <deque>

using namespace std;

class Solution {
public:
    int minimumLength(string s) {
        deque<char> d(s.begin(), s.end());

        while (d.size() > 1 && d.front() == d.back()) {
            char character = d.front();
            while (!d.empty() && d.front() == character)
                d.pop_front();
            while (!d.empty() && d.back() == character)
                d.pop_back();
        }

        return d.size();
    }
};