#include <algorithm>

using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        int max_diff = 0;
        dfs(max_diff, root->left, root->val, root->val);
        dfs(max_diff, root->right, root->val, root->val);
        return max_diff;
    }

    void dfs(int& max_diff, TreeNode* node, int max_val, int min_val) {
        if (node == nullptr) {
            max_diff = max(max_diff, max_val-min_val);
            return;
        }
        if (node->val < min_val) {
            min_val = node->val;
        } else if (node->val > max_val) {
            max_val = node->val;
        } 
        dfs(max_diff, node->left, max_val, min_val);
        dfs(max_diff, node->right, max_val, min_val);
    }
};