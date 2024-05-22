#include <vector>
#include <iostream>
#include <deque>

using namespace std;

#define INF 2147483647

class Solution
{
public:
    vector<vector<int>> distanceToNearestDoor(const vector<vector<int>> &grid)
    {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> res(m, vector<int>(n, INF));

        deque<pair<int, int>> d;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 0)
                    d.push_back({i, j});
                if (grid[i][j] == -1)
                    res[i][j] = -1;
            }
        }

        vector<pair<int, int>> directions({{0, -1}, {0, 1}, {1, 0}, {-1, 0}});
        int dist = 0;
        while (!d.empty()) {
            int n = d.size();
            for (int i = 0; i < n; i++) {
                int x = d.front().first;
                int y = d.front().second;
                d.pop_front();
                if (x >= 0 && x < m && y >= 0 && y < n) {
                    if (grid[x][y] != -1 && res[x][y] == INF) {
                        res[x][y] = dist;
                        for (auto dir : directions)
                        {
                            d.push_back({x+dir.first, y+dir.second});
                        }
                    }
                }
            }
            dist++;
        }
        return res;
    }
};

int main()
{
    vector<vector<int>> grid({{INF, -1, 0, INF},
                              {INF, INF, INF, -1},
                              {INF, -1, INF, -1},
                              {0, -1, INF, INF}});
    auto res = Solution().distanceToNearestDoor(grid);
    for (int i = 0; i < grid.size(); i++)
    {
        for (int j = 0; j < grid.size(); j++)
        {
            cout << res[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}