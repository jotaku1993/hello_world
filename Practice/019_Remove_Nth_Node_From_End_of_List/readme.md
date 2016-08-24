Use two pointers or scan the list twice.

It is better to build a dummy node for the return, since the head node may be delete. Connect the head to the dummy node, and return dummy->next, it helps you to consider less conditions.
