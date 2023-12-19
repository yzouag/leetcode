#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> row(m, 0);
        vector<int> col(n, 0);

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                row[i] += grid[i][j];
            }
        }

        for (int j=0; j<n; j++) {
            for (int i=0; i<m; i++) {
                col[j] += grid[i][j];
            }
        }

        vector<vector<int>> diff(m, vector<int>(n));
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                diff[i][j] = 2*row[i] - m + 2*col[j] - n;
            }
        }
        return diff;
    }
};