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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1==NULL && l2==NULL) return NULL;
        ListNode * ret = new ListNode(0);
        ListNode * cur = ret;
        
        while(l1!=NULL && l2!=NULL){
            if (l1->val < l2->val){
                cur->val = l1->val;
                l1 = l1->next;
            } else {
                cur->val = l2->val;
                l2 = l2->next;
            }
            cur->next = new ListNode(0);
            cur = cur->next;
        }
        if (l1!=NULL){
            cur->val = l1->val;
            cur->next = l1->next;
        }
        if (l2!=NULL){
            cur->val = l2->val;
            cur->next = l2->next;
        }
        
        return ret;
    }
};
