#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        unordered_set<char> trucks;
        int result = 0;
        for (int i=garbage.size()-1; i >= 0; i--) {
            if (trucks.size() < 3) {
                if (trucks.find('M') == trucks.end() && garbage[i].find('M') != string::npos) {
                    trucks.insert('M');
                }
                if (trucks.find('P') == trucks.end() && garbage[i].find('P') != string::npos) {
                    trucks.insert('P');
                }
                if (trucks.find('G') == trucks.end() && garbage[i].find('G') != string::npos) {
                    trucks.insert('G');
                }
            }
            result += garbage[i].size();
            if (i > 0)
                result += trucks.size() * travel[i-1];
        }
        return result;
    }
};