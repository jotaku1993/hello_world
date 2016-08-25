/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head==NULL || head->next==NULL) return head;
        
        ListNode * cur = head;
        
        int tmp = cur->val;
        while (cur->next!=NULL) {
            if (tmp == cur->next->val) {
                cur->next = cur->next->next;
            } else {
                cur = cur->next;
                tmp = cur->val;
            }
        }
        return head;
    }
};
