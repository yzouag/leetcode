#include <vector>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int length = 0;
        ListNode* curr = head;
        while (curr != nullptr) {
            curr = curr->next;
            length++;
        }
        int each_part_length = length/k;
        int extra_one_counts = length%k;
        vector<ListNode*> res;
        for (int i=0; i<k; i++) {
            res.push_back(head);
            int steps = each_part_length + (i<extra_one_counts? 1:0);
            for (int j=0; j<steps-1; j++) {
                head = head->next;
            }
            if (head->next) {
                ListNode* prev = head;
                head = head->next;
                prev->next = nullptr;
            }
        }
        return res;
    }
};