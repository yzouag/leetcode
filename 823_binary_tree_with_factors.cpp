#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int numFactoredBinaryTrees(vector<int> &arr)
    {
        unordered_map<int, long> node_treeCounts;

        sort(arr.begin(), arr.end());

        long mod = 1e9 + 7;

        long res = 0;

        for (int i = 0; i < arr.size(); i++)
        {
            long count = 1;
            for (int j = 0; j < i; j++)
            {
                if ((long)arr[j] * (long)arr[j] > (long)arr[i])
                    continue;
                if (arr[i] % arr[j] == 0)
                {
                    long left = arr[j];
                    long right = arr[i] / arr[j];
                    if (left == right)
                        count += node_treeCounts[left] * node_treeCounts[right];
                    else
                        count += 2 * node_treeCounts[left] * node_treeCounts[right];
                }
            }
            node_treeCounts[arr[i]] = count;
            res += count % mod;
            res %= mod;
        }
        return (int)res;
    }
};