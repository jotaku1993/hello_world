/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
private:
    ListNode * p = NULL;
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        p = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        ListNode * cur = p;
        int ret = cur->val;
        int cnt = 1;
        while (cur != NULL){
            if (rand()%cnt == 0){
                ret = cur->val;
            }
            cur = cur->next;
            cnt++;
        }
        return ret;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
