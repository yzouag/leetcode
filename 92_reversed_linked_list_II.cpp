
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) {
            return;
        }

        ListNode dummy(0, head);
        ListNode* curr = &dummy;
        ListNode* prev = head;
        while (curr->val != left) {
            curr = curr->next;
            prev = prev->next;
        }
        ListNode* next = curr->next;
        while (curr->val != right) {
            ListNode* temp = curr;
            curr = next;
            next = next->next;
            curr->next = temp;
        }
        prev->next->next = next;
        prev->next = curr;
        return dummy.next;
    }
};