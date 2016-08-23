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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode * ret = new ListNode(0);
        ListNode * cur = ret;
        
        int sum = 0;
        while(l1!=NULL || l2!=NULL || sum>0){
            if (l1 != NULL){
                sum = sum + l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL){
                sum = sum + l2->val;
                l2 = l2->next;
            }
            cur->val = sum % 10;
            sum = sum / 10;
            
            if (l1==NULL && l2==NULL &&sum==0) break;
            cur->next = new ListNode(0);
            cur = cur->next;
        }
        return ret;
    }
};
