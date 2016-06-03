Use fast and slow pointer to solve the problem.

Fast pointer has step 2 anf slow pointer has step 1.
If they can meet, that means there is a cycle in the linked list.
Otherwise, return null.

Start from the meet node and the head, walk by step 1 and they will meet at the cycle start point firstly. And it is the result.
