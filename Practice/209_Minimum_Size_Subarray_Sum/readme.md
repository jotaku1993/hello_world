First, exclude some special cases that may return 0.

Then, use two pointers, one fast and one slow to walk through the array.

Fast pointer walks until the sum larger than the object, then walk the slow and subtract until smaller than the object. Compare the min length when moving the slow pointer.
