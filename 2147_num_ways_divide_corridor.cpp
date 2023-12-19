#include <string>

using namespace std;

class Solution {
public:
    int numberOfWays(string corridor) {
        int num_chairs = 0;
        for (auto obj : corridor) {
            if (obj == 'S')
                num_chairs ++;
        }
        
        if (num_chairs % 2 != 0 || num_chairs < 2) {
            return 0;
        }

        int counts = 0;
        long result = 1;
        int plants = 0;
        int index = 0;
        int mod = 1e9 + 7;

        while (counts <= num_chairs-2) {
            if (corridor[index] == 'S') {
                if (counts%2 == 0 && counts > 1) {
                    result *= (plants+1);
                    result %= mod;
                    plants = 0;
                }
                counts++;
            } else {
                if (counts >= 2 && counts%2==0) {
                    plants++;
                }
            }

            index++;
        }

        return (int)result;
    }
};