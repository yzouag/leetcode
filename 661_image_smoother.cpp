#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        int m = img.size();
        int n = img[0].size();
        vector<vector<int>> result(m, vector<int>(n));

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                int x_start = -1;
                int y_start = -1;
                int x_end = 1;
                int y_end = 1;
                if (i == 0) {
                    x_start = 0;
                }
                if (i == m-1) {
                    x_end = 0;
                }
                if (j == 0) {
                    y_start = 0;
                }
                if (j == n-1) {
                    y_end = 0;
                }
                int sum = 0;
                for (int x=x_start; x<=x_end; x++) {
                    for (int y=y_start; y<=y_end; y++) {
                        sum += img[i+x][j+y];
                    }
                }
                result[i][j] = sum/((x_end-x_start+1)*(y_end-y_start+1));
            }
        }
        return result;
    }
};