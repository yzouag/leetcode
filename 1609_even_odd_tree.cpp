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
    bool isEvenOddTree(TreeNode* root) {
        deque<TreeNode*> node_deque;
        node_deque.push_back(root);

        bool is_odd_level = false;
        while (!node_deque.empty()) {
            int length = node_deque.size();
            int prev;
            for (int i=0; i<length; i++) {
                TreeNode* node = node_deque.front();
                int val = node->val;
                if (is_odd_level) {
                    if (val % 2 == 1)
                        return false;
                    if (i > 0 && val >= prev)
                        return false;
                } else {
                    if (val % 2 == 0)
                        return false;
                    if (i > 0 && val <= prev)
                        return false;
                }
                prev = val;
                node_deque.pop_front();

                if (node->left)
                    node_deque.push_back(node->left);

                if (node->right)
                    node_deque.push_back(node->right);
            }
            is_odd_level = !is_odd_level;
        }
        return true;
    }
};