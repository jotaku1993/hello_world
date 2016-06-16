Use dynamic programming.

One variable to save not choosing temporary house, another to save choosing.

Recurrent function:
OPT_not(n) = OPT(n-1) or OPT_not(n-1)
OPT(n) = OPT_not(n-1) + money[i]

finally return the max of OPT_not(n) and OPT(n)

Since here we have a loop, go through the algorithm from 1 -> l-1 and 2 -> l, compare the max, we will obtain the result.
