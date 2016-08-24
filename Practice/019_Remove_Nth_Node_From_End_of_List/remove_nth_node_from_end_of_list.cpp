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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode * nHead = new ListNode(0);
        nHead->next = head;
        ListNode * fast = nHead;
        ListNode * slow = nHead;
        for (int i=n; i>0; i--){
            fast = fast->next;
        }
        cout << fast->val <<endl;
        while(fast->next!=NULL){
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;
        return nHead->next;
    }
};
