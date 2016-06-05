Use binary search to do it, recursively.

We need to find the peak, but not the maximum value. So, local maximum is accepted.

When the search window converge to the peak point, return the position.

Convergence condition: mid point larger than both side or mid point is the edge of the window.
