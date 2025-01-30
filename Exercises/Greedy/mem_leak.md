# Incremental Memory Leak

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/incremental-memory-leak/description/).

## Initial Approach

To solve this exercise, I implemented an `iterative simulation` of the memory allocation process:

1. Start with a counter `i = 1`, representing the current second.

1. In each iteration:

   - Determine which memory stick has more available memory (or default to the first stick if both are equal).

   - Subtract `i` bits from the selected memory stick.

   - If the subtraction results in negative memory (indicating insufficient memory), the program crashes. Return the crash time (`i`) and the remaining memory in both sticks.

   - If there is enough memory, increment `i` and repeat the process.

1. The simulation continues until the program crashes, ensuring that all memory allocation steps are accurately tracked.

This approach ensures that the program's behavior is simulated step by step, and the crash condition is detected efficiently.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(√m)`, where m is the initial total memory (`memory1 + memory1`)

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
