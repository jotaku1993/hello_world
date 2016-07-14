Use dynamic programming, but not the best method.
For every element, scan the elements before them, if larger, +1; if smaller, keep the same, then use the largest one as the ans of this element.
