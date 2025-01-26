# Sort Array By Parity

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/sort-array-by-parity/description/).

## Initial Approach

The algorithm uses a **two-pointer-like technique** to efficiently sort the array by parity. One pointer (even_index) is used to track the position where the next even number should go, while the second pointer is implicitly the loop index (`i`) that iterates through the array.

For each element in the array:

- If the current number is even (`nums[i] % 2 == 0`), it is swapped with the element at `even_index`. This moves the even number to the front of the array.

- After the swap, `even_index` is incremented to point to the next position for an even number.

By iterating through the array once and swapping only when necessary, the algorithm avoids creating additional arrays, making it both time-efficient and memory-efficient.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the array.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
