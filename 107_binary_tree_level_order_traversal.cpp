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

class Solution
{
public:
    vector<vector<int>> levelOrderBottom(TreeNode *root)
    {
        int d = depth(root);
        vector<vector<int>> res(d, vector<int>{});
        if (d == 0)
            return res;

        queue<TreeNode *> q;
        q.push(root);
        int curr_d = 1;

        while (q.size() > 0)
        {
            int s = q.size();
            for (int i = 0; i < s; i++)
            {
                TreeNode *curr = q.front();
                q.pop();
                if (curr->left)
                    q.push(curr->left);
                if (curr->right)
                    q.push(curr->right);
                res[d - curr_d].push_back(curr->val);
            }
            curr_d++;
        }

        return res;
    }
    int depth(TreeNode *node)
    {
        if (!node)
            return 0;
        return max(depth(node->left), depth(node->right)) + 1;
    }
};