#include <vector>

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
    int averageOfSubtree(TreeNode* root) {
        int result = 0;
        dfs(result, root);
        return result;
    }

    // return [sum, num_nodes]
    vector<int> dfs(int& result, TreeNode* node) {
        if (node == nullptr) {
            return {0, 0};
        }

        auto left = dfs(result, node->left);
        auto right = dfs(result, node->right);

        int sums = node->val+left[0]+right[0];
        int nums = 1+left[1]+right[1];

        if (sums/nums == node->val) {
            result += 1;
        }

        return {sums, nums};
    }
};