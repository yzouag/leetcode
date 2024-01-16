#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <queue>

using namespace std;

// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// this question is same as find the farthest node of the given node
class Solution
{
public:
    // int amountOfTime(TreeNode* root, int start) {
    //     unordered_map<int, vector<int>> adj_list;
    //     dfs(root, adj_list);

    //     unordered_set<int> visited;
    //     queue<int> q;
    //     q.push(start);
    //     visited.insert(start);

    //     int result = -1;
    //     while (!q.empty()) {
    //         result++;
    //         int length = q.size();

    //         for (int i=0; i<length; i++) {
    //             int node = q.front();
    //             q.pop();

    //             for (int neighbor : adj_list[node]) {
    //                 if (visited.find(neighbor) != visited.end())
    //                     continue;
    //                 q.push(neighbor);
    //                 visited.insert(neighbor);
    //             }
    //         }
    //     }

    //     return result;
    // }

    // void dfs(TreeNode* root, unordered_map<int, vector<int>>& adj_list) {
    //     if (root->left) {
    //         adj_list[root->val].push_back(root->left->val);
    //         adj_list[root->left->val].push_back(root->val);
    //         dfs(root->left, adj_list);
    //     }

    //     if (root->right) {
    //         adj_list[root->val].push_back(root->right->val);
    //         adj_list[root->right->val].push_back(root->val);
    //         dfs(root->right, adj_list);
    //     }
    // }

    // do a standard dfs for depth.
    // 1. when the start is encountered for the first time STORE THE BELOW DEPTH and return -1 which marks the start of length that belongs to other side
    // 2. if the depth is negative ( which will be due to start) add the STORED depth with other side length and calculate max now from both lengths.
    // 3. if the depths are not negative (means we never got start) simply return standard depth formula

    int dfs(TreeNode *root, int &ans, int &start)
    {
        if (root == NULL)
            return 0;
        int l = dfs(root->left, ans, start);
        int r = dfs(root->right, ans, start);

        if (root->val == start)
        {
            // point no 1.
            ans = max(l, r);
            return -1;
        }
        else if (l >= 0 && r >= 0)
        {
            // point no 3.
            return max(l, r) + 1;
        }
        else
        {
            // point no 2.
            ans = max(ans, abs(l) + abs(r)); // if choose the current node as the root node
            return min(l, r) - 1; // one path will be positive, one path negative, deduct one more depth to the negative path and return
        }
    }

    int amountOfTime(TreeNode *root, int start)
    {
        int ans = 0;
        dfs(root, ans, start);
        return ans;
    }
};