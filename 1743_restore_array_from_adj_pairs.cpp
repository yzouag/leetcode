#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        int n = adjacentPairs.size() + 1;
        unordered_map<int, vector<int>> adj_list;
        for (auto pair : adjacentPairs) {
            adj_list[pair[0]].push_back(pair[1]);
            adj_list[pair[1]].push_back(pair[0]);
        }

        int start;
        for (auto kvpair : adj_list) {
            if (kvpair.second.size() == 1) {
                start = kvpair.first;
                break;
            } 
        }

        unordered_set<int> visited;
        vector<int> result;
        dfs(result, visited, adj_list, start);
        return result;
    }

    void dfs(vector<int>& result, unordered_set<int>& visited, unordered_map<int, vector<int>>& adj_list, int node) {
        if (visited.find(node) != visited.end()) {
            return;
        }

        visited.insert(node);
        result.push_back(node);

        for (int neightbor : adj_list[node]) {
            dfs(result, visited, adj_list, neightbor);
        }
    }
};