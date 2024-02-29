#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    string shortestCommonSupersequence(string s1, string s2)
    {
        int n = s1.size();
        int m = s2.size();
        vector<vector<int>> t(n + 1, vector<int>(m + 1, 0)); // table generated while computing LCS length
        string res;                                          // result
        // compute LCS length using tabulation
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= m; j++)
            {
                if (s1[i - 1] == s2[j - 1])
                    t[i][j] = 1 + t[i - 1][j - 1];
                else
                    t[i][j] = max(t[i - 1][j], t[i][j - 1]);
            }
        }
        // print lcs
        int i = n, j = m;
        while (i > 0 && j > 0)
        {
            if (s1[i - 1] == s2[j - 1])
            {
                res.push_back(s1[i - 1]);
                i--;
                j--;
            }
            else
            {
                if (t[i - 1][j] > t[i][j - 1])
                {
                    res.push_back(s1[i - 1]);
                    i--;
                }
                else
                {
                    res.push_back(s2[j - 1]);
                    j--;
                }
            }
        }
        while (i > 0) // if s1 characters are still left
        {
            res.push_back(s1[i - 1]);
            i--;
        }
        while (j > 0) // if s2 characters are still left
        {
            res.push_back(s2[j - 1]);
            j--;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};