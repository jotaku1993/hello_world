Use dynamic programming, maybe not?

Record the previous ugly numbers, and also use three index to record the position that we should multiply 2, 3 and 5.

New ugly number = min(idx2 * 2, idx3 * 3, idx5 * 5)

After we get the new ugly number, update the index until they multiply 2, 3 and 5 no larger than the new ugly number.
