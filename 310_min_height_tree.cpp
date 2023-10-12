#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) {
            return {0};
        }
        
        vector<int> indegrees(n, 0);
        vector<vector<int>> adj_list(n, vector<int>{});
        deque<int> one_degree;
        
        for (const auto& edge : edges) {
            indegrees[edge[0]]++;
            indegrees[edge[1]]++;
            adj_list[edge[0]].push_back(edge[1]);
            adj_list[edge[1]].push_back(edge[0]);
        }

        for (int i=0; i<n; i++) {
            if (indegrees[i] == 1)
                one_degree.push_back(i);
        }

        int remain_nodes = n;
        while (remain_nodes > 2)
        {
            int n = one_degree.size();
            for (int i=0; i<n; i++) {
                int node = one_degree.front();
                for (const int &neighbor : adj_list[node]) {
                    indegrees[neighbor]--;
                    if (indegrees[neighbor] == 1)
                        one_degree.push_back(neighbor);
                }
                one_degree.pop_front();
            }
            remain_nodes -= n;
        }
        return vector<int>(one_degree.begin(), one_degree.end());
    }
};