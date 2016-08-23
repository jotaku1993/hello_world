Use hash table to record the visited element.

In every iteration, find the target-nums[i] in the hashtable, if exist, return them. Otherwise, add the nums[i] to the hashtable and go to next iteration.

Runtime is O(n).
