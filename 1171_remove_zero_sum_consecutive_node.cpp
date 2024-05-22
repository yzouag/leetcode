#include <unordered_map>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// [1, 2, -2, -1, 3]
// [0, 1,  3,  1, 0, 3]

// [1,3,2,-3,-2,5,5,-5,1]
// [0,1,4,6,3,1,6,11,6,7]
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        int accum = 0;
        ListNode dummy({0, head});
        unordered_map<int, ListNode*> prefix_node_map;
        prefix_node_map[0] = &dummy;
        while (head != nullptr) {
            accum += head->val;
            if (prefix_node_map.find(accum) != prefix_node_map.end()) {
                auto node = prefix_node_map[accum]->next;
                int prefix = accum + node->val;
                while (prefix != accum) {
                    prefix_node_map.erase(prefix);
                    node = node->next;
                    prefix += node->val;
                }
                prefix_node_map[accum]->next = head->next;
                prefix_node_map.erase(accum);
            } else {
                prefix_node_map[accum] = head;
            }
            head = head->next;
        }
        return dummy.next;
    }
};