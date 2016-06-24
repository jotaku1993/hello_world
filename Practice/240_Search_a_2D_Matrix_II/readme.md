Scan the matrix from the right-top:

If small than the target, that means this row will not contain the element, go to next row.

If larger than the target, that means this columnwill not coontain the element, go to the previous column.

If the same as the target, return true.

When it goes to the boundary again, stop the algorithm.
