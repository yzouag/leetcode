#include <vector>
#include <numeric>
#include <unordered_map>

using namespace std;

class DisjointSet {
private:
    vector<int> ranks;

public:
    vector<int> parents;
    DisjointSet(int size) {
        for (int i=0; i<size; i++)
            parents.push_back(i);

        ranks.resize(size, 0);
    }

    int find(int node) {
        if (parents[node] == node)
            return node;
        parents[node] = find(parents[node]);
        return parents[node];
    }

    bool is_connected(int a, int b) {
        return find(a) == find(b);
    }

    void join_nodes(int a, int b) {
        int a_p = find(a);
        int b_p = find(b);

        if (ranks[a_p] > ranks[b_p]) {
            parents[b_p] = a_p;
        } else if (ranks[a_p] == ranks[b_p]) {
            parents[b_p] = a_p;
            ranks[a_p] += 1;
        } else {
            parents[a_p] = b_p;
        }
    }

    bool all_connected() {
        int parent_is_itself = 0;
        for (int i=0; i<parents.size(); i++) {
            if (i == parents[i])
                parent_is_itself++;
            if (parent_is_itself > 1)
                return false;
        }
        return true;
    }
};

class Solution {
public:
    bool canTraverseAllPairs(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> visited;

        DisjointSet u(n);
        for (int i=0; i<n; i++) {
            if (visited.find(nums[i]) != visited.end()) {
                u.parents[i] = visited[i];
                continue;
            }
            visited[nums[i]] = i;
            for (int j=i+1; j<n; j++) {
                if (u.is_connected(i, j))
                    continue;
                if (gcd(nums[i], nums[j]) != 1) {
                    u.join_nodes(i, j);
                }
            }
        }
        return u.all_connected();
    }
};