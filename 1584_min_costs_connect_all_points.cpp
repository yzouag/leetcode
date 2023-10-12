#include <vector>
#include <queue>
#include <iostream>

// two main algorithm for minimal spanning tree:
// 1. Prim's algorithm (dijkstra)
// arbitrary pick one point, find closest distance to vertex not in the spanning tree yet
// put that vertex in, include new edges
// 2. Kruskal algorithm
// sort edges in ascending order, if two nodes of edges are not connected, choose this edge.
using namespace std;

int mahattan_distance(const vector<int> &p1, const vector<int> &p2) {
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]);
}

class DSU {
    int n;
    vector<int> parent, size;
public:
    DSU(int n) {
        this->n = n;
        parent.resize(n, -1);
        size.resize(n, 1);
    }

    int find(int node) {
        if (parent[node] == -1) {
            return node;
        }
        parent[node] = find(parent[node]);
        return parent[node];
    }

    bool union_join(int u, int v) {
        u = find(u);
        v = find(v);

        if (u == v) {
            return false;
        }

        if (size[u] > size[v]) {
            swap(u, v);
        }
        parent[u] = v;
        size[v] += size[u]; // union by size
        return true;
    }
};

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        // Prim's algorithm
        // int n = points.size();
        // vector<bool> visited(n, false);
        // int nodes_visited = 0;
        // auto cmp = [&](pair<int, int> left, pair<int, int> right) {
        //     return left.second > right.second;
        // };
        // priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> queue(cmp);
        // queue.push({0, 0}); // {dest_node, distance}
        // int result = 0;

        // while (nodes_visited < n) {
        //     auto [node, dist] = queue.top();
        //     queue.pop();
        //     if (visited[node])
        //         continue;
            
        //     result += dist;
        //     visited[node] = true;
        //     nodes_visited ++;
        //     for (int v=0; v<n; v++) {
        //         if (visited[v])
        //             continue;
        //         queue.push({v, mahattan_distance(points[node], points[v])});
        //     }
        // }
        // return result;

        // Kruscal's algorithm
        int n = points.size();
        auto cmp = [&](vector<int> e1, vector<int> e2) {
            return e1[0] > e2[0];
        };
        priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> pq(cmp);
        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {
                pq.push({mahattan_distance(points[i], points[j]), i, j});
            }
        }
        int result = 0;
        DSU dsu(n);
        int edges = 0;
        while (edges < n-1) {
            auto edge = pq.top();
            pq.pop();
            if (dsu.union_join(edge[1], edge[2])) {
                edges += 1;
                result += edge[0];
            }
        }
        return result;
    }
};

int main() {
    vector<vector<int>> points = {{3,12},{-2,5},{-4,1}};
    cout << Solution().minCostConnectPoints(points) << endl;
}