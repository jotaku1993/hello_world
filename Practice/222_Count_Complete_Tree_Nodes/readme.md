Use binary search.

Since it is complete binary tree, it will be full in all levels except the last level. So we need to find the nodes in the last level.

But here, use binary search, compare the depth of left and right. If they are the same, it is perfect tree so the nodes are (2^)n-1; if not the same, recur to the left and right, do the same thing.
