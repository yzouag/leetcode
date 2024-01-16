#include <string>
#include <unordered_set>
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
    string parsePair(pair<int, int> point) {
        ostringstream os;
        os << point.first << "," << point.second;
        return os.str();
    }

    bool isPathCrossing(string path) {
        unordered_set<string> points;

        pair<int, int> start = {0, 0};
        points.insert(parsePair(start));
        for (auto p : path) {
            switch (p)
            {
            case 'N':
                start.second += 1;
                break;
            case 'E':
                start.first += 1;
                break;
            case 'W':
                start.first -= 1;
                break;
            case 'S':
                start.second -= 1;
                break;
            }
            if (points.find(parsePair(start)) != points.end()) {
                return true;
            }
            points.insert(parsePair(start));
        }
        return false;
    }
};