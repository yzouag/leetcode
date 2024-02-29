#include <vector>

using namespace std;

class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> prefix(m+1, vector<int>(n+1, 0));

        for (int i=1; i<=m; i++) {
            for (int j=1; j<=n; j++) {
                prefix[i][j] = matrix[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1];
            }
        }

        int result = 0;
        for (int x1=1; x1<=m; x1++) {
            for (int x2=1; x2<=n; x2++) {
                
            }
        }

        return result;
    }
};