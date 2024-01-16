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
private:
    vector<int> ans;
    int maxStreak = 0;
    int curStreak = 0;
    int currNum = -1;

public:
    vector<int> findMode(TreeNode* root) {
        dfs(root);
        return ans;
    }

    // inorder traversal will get all number in the ascending order
    void dfs(TreeNode* node) {
        if (node == nullptr)
            return;

        dfs(node->left);

        int num = node->val;
        if (num == currNum) {
            curStreak += 1;
        } else {
            curStreak = 1;
            currNum = num;
        }

        if (curStreak > maxStreak) {
            maxStreak = curStreak;
            ans = {num};
        } else if (curStreak == maxStreak) {
            ans.push_back(num);
        }

        dfs(node->right);
    }
};