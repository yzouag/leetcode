#include <string>

using namespace std;

class Solution {
public:
    bool winnerOfGame(string colors) {
        int alice = 0, bob = 0;
        int start = 0;
        if (colors.back() == 'A')
            colors.push_back('B');
        else
            colors.push_back('A');
        for (int i=1; i<colors.size(); i++) {
            if (colors[i] != colors[start]) {
                if (i-start > 2) {
                    if (colors[start] == 'A')
                        alice += i-start-2;
                    else
                        bob += i-start-2;
                }
                start = i;
            }
        }
        return alice > bob;
    }
};