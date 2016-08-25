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
    ListNode* swapPairs(ListNode* head) {
        if (head==NULL || head->next==NULL) return head;
        
        ListNode * dummy = new ListNode(0);
        dummy->next = head;
        
        ListNode * cur = dummy->next;
        ListNode * pre = dummy;
        while(cur!=NULL && cur->next!=NULL){
            ListNode * tmp = cur->next->next;
            
            pre->next = cur->next;
            pre = pre->next;
            pre->next = cur;
            cur->next = tmp;
            pre = pre->next;
            cur = cur->next;
        }
        return dummy->next;
    }
};
