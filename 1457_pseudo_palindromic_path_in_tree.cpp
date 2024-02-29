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
    int pseudoPalindromicPaths (TreeNode* root) {
        int res = 0;
        vector<int> counts(9, 0);
        dfs(root, counts, res);
        return res;
    }
    
    void dfs(TreeNode* node, vector<int> counts, int& res) {
        counts[node->val-1]++;
        if (node->left == nullptr && node->right == nullptr) {
            int odds = 0;
            for (int i=0; i<9; i++) {
                if (counts[i] % 2 == 1)
                    odds++;
            }
            if (odds <= 1)
                res++;
            return;
        }

        if (node->left)
            dfs(node->left, counts, res);
        if (node->right)
            dfs(node->right, counts, res);
    }
};