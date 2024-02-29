#include <deque>

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
    int findBottomLeftValue(TreeNode* root) {
        deque<TreeNode*> d;
        d.push_back(root);

        int result;
        while (!d.empty()) {
            int length = d.size();
            result = d.front()->val;
            for (int i=0; i<length; i++) {
                TreeNode* node = d.front();
                d.pop_front();
                if (node->left != nullptr)
                    d.push_back(node->left);
                if (node->right != nullptr)
                    d.push_back(node->right);
            }
        }

        return result;
    }
};