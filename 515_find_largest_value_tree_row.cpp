#include <vector>
#include <queue>

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
    vector<int> largestValues(TreeNode* root) {
        vector<int> res;

        if (!root) {
            return res;
        }

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int largest = INT32_MIN;
            int q_size = q.size();

            for (int i=0; i<q_size; i++) {
                auto node = q.front();
                q.pop();
                if (node->val > largest)
                    largest = node->val;
                if (node->left)
                    q.push(node->left);
                if (node->right)
                    q.push(node->right);
            }

            res.push_back(largest);
        }

        return res;
    }
};